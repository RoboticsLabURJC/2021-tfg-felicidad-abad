import subprocess
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

'''client.containers.run('ubuntu:latest', 'echo hello world')'''
''' Lo primero que hay que hacer es iniciar tanto el contenedor de bbdd,
como el del RADI para poder usar Selenium después'''
'''subprocess.Popen(f'docker start db_container',stdout=subprocess.PIPE,shell=True)'''
from .operations import create_user, create_exercise
import time
import sys
from environs import Env
import json
import re

subprocess.Popen(f'sudo docker start RADI',stdout=subprocess.PIPE,shell=True)
sys.path.append('academy/tests/')
env = Env()
env.read_env()

class TestLogin(LiveServerTestCase):

    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)

    def tearDown(self):
        self.selenium.quit()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()
        
        
class TestObstacleAvoidanceExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="obstacle_avoidance", name="Obstacle Avoidance")

    def tearDown(self):
        self.selenium.quit()
        

    def test_obstacle_avoidance_enter(self):
        '''self.selenium.get('%s%s' % (self.live_server_url, '/'))'''
        self.selenium.get("http://127.0.0.1:8000")
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()
        
        ## ENTER OBS AVOIDANCE & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()
        
        time.sleep(20)
        ace = self.selenium.find_element(By.ID,"editor")
        print(ace)
        '''editorele = ace.sendKeys("editor");
        editorele.setValue(code);
        ace.clear()
        self.selenium.execute_script("ace.edit('editor').setValue('probando')")
        
        print(subprocess.run(f'sudo docker exec -it RADI bash -c "source prepara.sh"', shell=True, capture_output=True))
        result = subprocess.run(f'sudo docker exec -it RADI bash -c "source prepara.sh"', shell=True, capture_output=True)'''
        print(".run")
        result = subprocess.run(f'sudo docker exec -it RADI bash -c "source prepara.sh"', shell=True, capture_output=True)
        '''
        print("popen")
        result = subprocess.Popen(f'sudo docker exec -it RADI bash -c "source prepara.sh"', stdout=subprocess.PIPE,shell=True)
        print(result)
        print("final")'''
        
        #Para tratar la respuesta que se devuelve en bytes y es rara
        print(result.stdout)
        print("intento tratar el string")
        pose3Duno = result.stdout.decode('utf-8')
        print(pose3Duno)
        pose3Duno = pose3Duno[pose3Duno.find("Pose3D"):pose3Duno.find("}")+1].replace('\r\n', ',')
        pose3Duno = pose3Duno.replace(',', '', 1)
        pose3Duno_rev = pose3Duno[::-1]
        pose3Duno_rev = pose3Duno_rev.replace(',', '', 1)
        pose3Duno = pose3Duno_rev[::-1]
        pose3Duno = pose3Duno[pose3Duno.find("{")-1::]
        pose3Duno = re.sub(r'\bY\b', r'"Y"', pose3Duno)
        string = pose3Duno.replace('x', '"x"').replace('Yaw', '"Yaw"').replace('Z', '"Z"').replace('H', '"H"').replace('Pitch', '"Pitch"').replace('Roll', '"Roll"').replace('quaternion', '"quaternion"').replace('timeStamp', '"timeStamp"').replace('[', '["').replace(']', '"]')
        data = json.loads(string)

        print("La posicion de la x es: ", data['x'])
        print("La posicion de la y es: ", data['Y'])
        
        # Para insertar el código en el editor
        actions = ActionChains(self.selenium)
        actions.move_to_element(ace).send_keys("from GUI import GUI\r\n from HAL import HAL\r\n # Enter sequential code!\r\n while True:\r\n# Enter iterative code!\r\n currentTarget = GUI.map.getNextTarget()\r\n GUI.map.targetx = currentTarget.getPose().x\r\n GUI.map.targety = currentTarget.getPose().y\r\n HAL.setV(2)).perform()")
        print("llegamos hasta actions")
        
        #Antes de que funcione sería necesario que conecte con el RADI
        self.selenium.find_element(By.ID, "launch-button").click()
        time.sleep(10)
        self.selenium.find_element(By.ID, "loadIntoRobot").click()
        time.sleep(20)
        print("ya ha cargado el codigo")
        
        self.selenium.find_element(By.ID, "submit").click()
        time.sleep(10)
        
        result2 = subprocess.run(f'sudo docker exec -it RADI bash -c "source prepara.sh"', shell=True, capture_output=True)
        print(result2)
        
        pose3Ddos = result2.stdout.decode('utf-8')
        pose3Ddos = pose3Ddos[pose3Ddos.find("Pose3D"):pose3Ddos.find("}")+1].replace('\r\n', ',')
        pose3Ddos = pose3Ddos.replace(',', '', 1)
        pose3Ddos_rev = pose3Ddos[::-1]
        pose3Ddos_rev = pose3Ddos_rev.replace(',', '', 1)
        pose3Ddos = pose3Ddos_rev[::-1]
        pose3Ddos = pose3Ddos[pose3Ddos.find("{")-1::]
        pose3Ddos = re.sub(r'\bY\b', r'"Y"', pose3Ddos)
        string2 = pose3Ddos.replace('x', '"x"').replace('Yaw', '"Yaw"').replace('Z', '"Z"').replace('H', '"H"').replace('Pitch', '"Pitch"').replace('Roll', '"Roll"').replace('quaternion', '"quaternion"').replace('timeStamp', '"timeStamp"').replace('[', '["').replace(']', '"]')
        data = json.loads(string2)
        
        print("La posicion de la x2 es: ", data['x'])
        print("La posicion de la y2 es: ", data['Y'])
   


