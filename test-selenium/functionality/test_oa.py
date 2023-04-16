from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


from .operations import create_user, create_exercise
import time
import sys
from environs import Env
import yaml
import subprocess

sys.path.append('academy/tests/')
env = Env()
env.read_env()

subprocess.Popen(f'sudo docker start RADI',stdout=subprocess.PIPE,shell=True)


class TestAceEditor(StaticLiveServerTestCase):
    def setUp(self):
        opts = Options()
        #opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="obstacle_avoidance", name="Obstacle Avoidance")

    def tearDown(self):
        self.selenium.quit()

    def test_insert_code(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()
        ## ENTER EXERCISE
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()
        time.sleep(1)
        ## Editor
        self.selenium.execute_script("ace.edit('editor').setValue('from GUI import GUI\\nfrom HAL import HAL\\nwhile True:\\n    HAL.setV(5)')")
        time.sleep(5)

        #Antes de que funcione sería necesario que conecte con el RADI
        self.selenium.find_element(By.ID, "launch-button").click()

        #Cerramos la alerta que se abre cuando ha conectado con el RADI
        alert = WebDriverWait(self.selenium, 60).until(EC.alert_is_present())
        alert.accept()

        #Cargar el código en el robot
        self.selenium.find_element(By.ID, "loadIntoRobot").click()
        print("ya ha cargado el codigo")

        WebDriverWait(self.selenium, 40).until(EC.invisibility_of_element_located((By.XPATH, '//ul[@style="display:inline-block"]')))

        self.selenium.find_element(By.ID, "submit").click()
        time.sleep(2)

        def processResponse (data):
            data = data.stdout.decode('utf-8')
            findPoseIndex = data.index("pose")
            findtwistIndex = data.index("twist")
            pose_yaml = yaml.safe_load(data[findPoseIndex:findtwistIndex])

            return pose_yaml

        #Primera consulta a la posición dada por el topic
        result1 = subprocess.run(f'sudo docker exec -it RADI bash -c "source /test_functionality/topic_f1.sh"', shell=True, capture_output=True)
        processedResponse1 = processResponse(result1)
        positions1 = {
            'x' : processedResponse1['pose']['pose']['position']['x'],
            'y' : processedResponse1['pose']['pose']['position']['y']
        }

        time.sleep(5)
        #Segunda consulta a la posición dada por el topic
        result2 = subprocess.run(f'sudo docker exec -it RADI bash -c "source /test_functionality/topic_f1.sh"', shell=True, capture_output=True)
        processedResponse2 = processResponse(result2)
        positions2 = {
            'x' : processedResponse2['pose']['pose']['position']['x'],
            'y' : processedResponse2['pose']['pose']['position']['y']
        }

        print(positions1)
        print(positions2)
        assert positions1 != positions2
