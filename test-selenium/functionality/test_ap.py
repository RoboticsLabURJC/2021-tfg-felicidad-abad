import subprocess
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException

''' Lo primero que hay que hacer es iniciar tanto el contenedor de bbdd,
como el del RADI para poder usar Selenium después'''
from .operations import create_user, create_exercise
import time
import sys
from environs import Env
import json
import re
import yaml

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
        self.password = "pass"
        self.user = create_user(username="admin_dummy", password=self.password)

    def tearDown(self):
        self.selenium.quit()

    def test_login(self):
        '''
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        '''
        self.selenium.get('http://127.0.0.1:8000/')
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()


class TestAutoparkingExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "pass"
        self.user = create_user(username="admin_dummy", password=self.password)
        self.exercise = create_exercise(exercise_id="autoparking", name="Autoparking")

    def tearDown(self):
        self.selenium.quit()


    def test_autoparking_enter(self):
        '''self.selenium.get('%s%s' % (self.live_server_url, '/'))'''
        self.selenium.get("http://127.0.0.1:8000")
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        time.sleep(15)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        def processResponse (data):
            data = data.stdout.decode('utf-8')
            findPoseIndex = data.index("pose")
            findtwistIndex = data.index("twist")
            pose_yaml = yaml.safe_load(data[findPoseIndex:findtwistIndex])

            return pose_yaml

        result1 = subprocess.run(f'sudo docker exec -it RADI bash -c "source /test_functionality/topic_taxi.sh"', shell=True, capture_output=True)
        processedResponse1 = processResponse(result1)
        print(processedResponse1)
        print(type(processedResponse1))
        positions1 = {
            'x' : processedResponse1['pose']['pose']['position']['x'],
            'y' : processedResponse1['pose']['pose']['position']['y']
        }

        time.sleep(5)
        result2 = subprocess.run(f'sudo docker exec -it RADI bash -c "source /test_functionality/topic_taxi.sh"', shell=True, capture_output=True)
        processedResponse2 = processResponse(result2)
        positions2 = {
            'x' : processedResponse2['pose']['pose']['position']['x'],
            'y' : processedResponse2['pose']['pose']['position']['y']
        }

        print(positions1)
        print(positions2)
        assert positions1 != positions2
