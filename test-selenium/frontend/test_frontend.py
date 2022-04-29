from django.test import LiveServerTestCase
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


class TestFollowLineExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="follow_line", name="Follow Line")

    def tearDown(self):
        self.selenium.quit()

    def test_follow_line_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_follow_line_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_follow_line_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_follow_line_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_follow_line_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_follow_line_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_follow_line_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_follow_line_gazebo_button(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "gazebo_button")
        save_button.click()

    def test_follow_line_teleop_button(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "teleop_button")
        save_button.click()

    def test_follow_line_efficacy_button(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "efficacy")
        save_button.click()


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

        ## ENTER EXERCISE
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_obstacle_avoidance_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER  OBS AVOIDANCE & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_obstacle_avoidance_theory(self):
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

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_obstacle_avoidance_forum(self):
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

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_obstacle_avoidance_exercise_button(self):
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

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_obstacle_avoidance_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_obstacle_avoidance_save(self):
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

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_obstacle_avoidance_gazebo(self):
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

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()

    def test_obstacle_avoidance_efficacy(self):
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

        time.sleep(2)
        ## EFFICACY BUTTON
        efficacy_button = self.selenium.find_element(By.ID, "efficacy")
        efficacy_button.click()


class TestVacuumCleanerExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="vacuum_cleaner", name="Vacuum Cleaner")

    def tearDown(self):
        self.selenium.quit()

    def test_vacuum_cleaner_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
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

    def test_vacuum_cleaner_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER VCLEANER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_vacuum_cleaner_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER VCLEANER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_vacuum_cleaner_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER VCLEANER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_vacuum_cleaner_exercise_button(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER VCLEANER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_vacuum_cleaner_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER VCLEANER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_vacuum_claner_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER VCLEANER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_vacuum_cleaner_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER VCLEANER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()

    def test_vacuum_cleaner_efficacy(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER VCLEANER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## EFFICACY BUTTON
        efficacy_button = self.selenium.find_element(By.ID, "efficacy")
        efficacy_button.click()


class TestVacuumCleanerLocExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="vacuum_cleaner_loc", name="Localized Vacum Cleaner")

    def tearDown(self):
        self.selenium.quit()

    def test_vacuum_cleaner_loc_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
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

    def test_vacuum_cleaner_loc_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_vacuum_cleaner_loc_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_vacuum_cleaner_loc_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_vacuum_cleaner_loc_exercise_button(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_vacuum_cleaner_loc_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_vacuum_claner_loc_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_vacuum_cleaner_loc_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()

    def test_vacuum_cleaner_loc_efficacy(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## EFFICACY BUTTON
        efficacy_button = self.selenium.find_element(By.ID, "efficacy")
        efficacy_button.click()


class TestColorFilterExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="color_filter", name="Color Filter")

    def tearDown(self):
        self.selenium.quit()

    def test_color_filter_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_color_filter_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_color_filter_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_color_filter_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_color_filter_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_color_filter_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_color_filter_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()


class Test3DReconstructionExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="3d_reconstruction", name="3D Reconstruction")

    def tearDown(self):
        self.selenium.quit()

    def test_3d_reconstruction_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_3d_reconstruction_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_3d_reconstruction_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_3d_reconstruction_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_3d_reconstruction_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_3d_reconstruction_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_3d_reconstruction_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_3d_reconstruction_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()


class TestOpticalFlowTeleopExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="opticalflow_teleop", name="Optical Flow Teleop")

    def tearDown(self):
        self.selenium.quit()

    def test_opticalflow_teleop_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_opticalflow_teleop_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_opticalflow_teleop_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_opticalflow_teleop_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_opticalflow_teleop_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_opticalflow_teleop_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_opticalflow_teleop_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_opticalflow_teleop_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()


class TestGlobalNavigationExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="global_navigation", name="Global Navigation")

    def tearDown(self):
        self.selenium.quit()

    def test_oglobal_navigation_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_global_navigation_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_global_navigation_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_global_navigation_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER GLOB. NAVIGATION & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_global_navigation_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_global_navigation_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_global_navigation_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_global_navigation_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()


class TestLaserMappingExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="laser_mapping", name="Laser Mapping")

    def tearDown(self):
        self.selenium.quit()

    def test_laser_mapping_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_laser_mapping_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_laser_mapping_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_laser_mapping_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_laser_mapping_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_laser_mapping_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_laser_mapping_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_laser_mapping_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()

    def test_laser_mapping_teleop(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "teleop_button")
        gazebo_button.click()


class TestFollowLineGameExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="follow_line_game", name="Follow Line Game")

    def tearDown(self):
        self.selenium.quit()

    def test_follow_line_game_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_follow_line_game_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_follow_line_game_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_follow_line_game_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_follow_line_game_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_follow_line_game_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_follow_line_game_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_follow_line_game_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()

    def test_follow_line_game_teleop(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "teleop_button")
        gazebo_button.click()


class TestRescuePeopleExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="rescue_people", name="Rescue People")

    def tearDown(self):
        self.selenium.quit()

    def test_rescue_people_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_rescue_people_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_rescue_people_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_rescue_people_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_rescue_people_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_rescue_people_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_rescue_people_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_rescue_people_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()


class TestMontecarloVisualLocExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="montecarlo_visual_loc", name="Montecarlo Visual Loc")

    def tearDown(self):
        self.selenium.quit()

    def test_montecarlo_visual_loc_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_montecarlo_visual_loc_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_montecarlo_visual_loc_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_montecarlo_visual_loc_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_montecarlo_visual_loc_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_montecarlo_visual_loc_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_montecarlo_visual_loc_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_montecarlo_visual_loc_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()


class TestDroneCatMouseExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="drone_cat_mouse_game", name="Drone Cat Mouse")

    def tearDown(self):
        self.selenium.quit()

    def test_drone_cat_mouse_game_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_drone_cat_mouse_game_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_drone_cat_mouse_game_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_drone_cat_mouse_game_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_drone_cat_mouse_game_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_drone_cat_mouse_game_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_drone_cat_mouse_game_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_drone_cat_mouse_game_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()

    def test_drone_cat_mouse_game_evaluator(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "eval_button")
        gazebo_button.click()


class TestAutoparkingExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="autoparking", name="Autoparking")

    def tearDown(self):
        self.selenium.quit()

    def test_autoparking_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_autoparking_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_autoparking_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_autoparking_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_autoparking_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_autoparking_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_autoparking_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_autoparking_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()


class TestCarJunctionExercise(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password)
        self.exercise = create_exercise(exercise_id="car_junction", name="Car Junction")

    def tearDown(self):
        self.selenium.quit()

    def test_car_junction_enter(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()

    def test_car_junction_launch(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()

    def test_car_junction_theory(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER COLOR FILTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()

    def test_car_junction_forum(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

    def test_car_junction_exercise(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()

    def test_car_junction_console(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()

    def test_car_junction_save(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER LASER MAPPING & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()

    def test_car_junction_gazebo(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        print(self.selenium.title)
        WebDriverWait(self.selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/academy/login"]'))).click()

        username = self.selenium.find_element(By.NAME, "username")
        username.send_keys(self.user.username)
        password = self.selenium.find_element(By.NAME, "password")
        password.send_keys(self.password)
        self.selenium.find_element(By.XPATH, "//input[@class='fadeIn fourth']").click()

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()
