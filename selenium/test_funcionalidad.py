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

print(1)
subprocess.Popen(f'sudo docker start RADI',stdout=subprocess.PIPE,shell=True)
print(2)

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
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
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
        
        actions = ActionChains(self.selenium)
        actions.move_to_element(ace).send_keys("myusername").perform()
        print("llegamos hasta actions")
        '''editorele = ace.sendKeys("editor");
        editorele.setValue(code);
        ace.clear()
        self.selenium.execute_script("ace.edit('editor').setValue('probando')")
        
        print(subprocess.run(f'sudo docker exec -it RADI bash -c "source prepara.sh"', shell=True, capture_output=True))
        result = subprocess.run(f'sudo docker exec -it RADI bash -c "source prepara.sh"', shell=True, capture_output=True)'''
        result = subprocess.run('sudo docker exec -it RADI bash -c "source prepara.sh"', shell=True, capture_output=True)
        print(result)
        print("final")
        
        pose3Duno = result.stdout[result.stdout.find("Pose3D"):result.stdout.find("}")+1].replace('\r\n', ',')
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
 
'''       
        print('_______________')
        print(result.CompletedProcess.X)  
        print('ejercicio')
        subprocess.Popen(f'sudo docker exec -it RADI /bin/bash',stdout=subprocess.PIPE,shell=True)
        print("111")
        subprocess.Popen(f'sudo docker exec -it RADI roscore',stdout=subprocess.PIPE,shell=True)
        print(subprocess.run(f'sudo docker exec -it RADI /bin/bash -c "export PATH=$PATH:/opt/ros/noetic/bin:/opt/gradle/gradle-6.3-rc-4/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/VirtualGL/bin:/opt/TurboVNC/bin"',shell=True,capture_output=True))
        print(subprocess.run(f'sudo docker exec -it RADI exec bash',shell=True,capture_output=True))
        print(subprocess.run(f'sudo docker exec -it RADI bin/bash -c "echo $PATH"',shell=True,capture_output=True))
        print('---------')
        ejecucion = subprocess.run(f'sudo docker exec -it RADI python3 /RoboticsAcademy/exercises/obstacle_avoidance/testing.py',shell=True,capture_output=True)
        print(ejecucion)
        print('eo')
'''


