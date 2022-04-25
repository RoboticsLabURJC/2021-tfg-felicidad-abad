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


class TestFollowLineLaunchButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="follow_line", name="Follow Line")


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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()


class TestFollowLineTheoryButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="follow_line", name="Follow Line")

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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()


class TestFollowLineForumButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="follow_line", name="Follow Line")

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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()


class TestFollowLineExerciseButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="follow_line", name="Follow Line")

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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()

        exercise = self.selenium.find_element(By.ID, "open-exercise")
        exercise.click()


class TestFollowLineConsoleButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="follow_line", name="Follow Line")

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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()


class TestFollowLineSaveButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="follow_line", name="Follow Line")


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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()


class TestFollowLineGazeboButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="follow_line", name="Follow Line")


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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()


class TestFollowLineTeleopButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="follow_line", name="Follow Line")


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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## TELEOPERATION BUTTON
        teleop_button = self.selenium.find_element(By.ID, "teleop_button")
        teleop_button.click()


class TestFollowLineEfficacyButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="follow_line", name="Follow Line")


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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## EFFICACY BUTTON
        efficacy_button = self.selenium.find_element(By.ID, "efficacy")
        efficacy_button.click()


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

        ## ENTER EXERCISE
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()


class TestObstacleAvoidanceLaunchButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="obstacle_avoidance", name="Obstacle Avoidance")


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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()


class TestObstacleAvoidanceTheoryButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="obstacle_avoidance", name="Obstacle Avoidance")

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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()


class TestObstacleAvoidanceForumButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="obstacle_avoidance", name="Obstacle Avoidance")

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
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()


class TestObstacleAvoidanceExerciseButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="obstacle_avoidance", name="Obstacle Avoidance")

    def tearDown(self):
        self.selenium.quit()

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


class TestObstacleAvoidanceConsoleButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="obstacle_avoidance", name="Obstacle Avoidance")

    def tearDown(self):
        self.selenium.quit()

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


class TestObstacleAvoidanceSaveButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="obstacle_avoidance", name="Obstacle Avoidance")


    def tearDown(self):
        self.selenium.quit()

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

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()


class TestObstacleAvoidanceGazeboButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="obstacle_avoidance", name="Obstacle Avoidance")


    def tearDown(self):
        self.selenium.quit()

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

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()


class TestObstacleAvoidanceEfficacyButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="obstacle_avoidance", name="Obstacle Avoidance")


    def tearDown(self):
        self.selenium.quit()

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

        ## ENTER & CLOSE MODAL
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
        self.exercise = create_exercise(exercise_id="vacuum_cleaner", name="Vacum Cleaner")


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


class TestVacuumCleanerLaunchButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner", name="Vacuum Cleaner")


    def tearDown(self):
        self.selenium.quit()

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

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(5)
        ## LAUNCH BUTTON
        launch_button = self.selenium.find_element(By.ID, "launch-button")
        launch_button.click()


class TestVacuumCleanerTheoryButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner", name="Vacuum Cleaner")

    def tearDown(self):
        self.selenium.quit()

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

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CHECK THEORY
        theory_button = self.selenium.find_element(By.ID, "open-theory")
        theory_button.click()


class TestVacuumCleanerForumButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner", name="Vacuum Cleaner")

    def tearDown(self):
        self.selenium.quit()

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

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GO TO FORUM
        forum = self.selenium.find_element(By.ID, "open-forum")
        forum.click()


class TestVacuumCleanerExerciseButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner", name="Vacuum Cleaner")

    def tearDown(self):
        self.selenium.quit()

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


class TestVacuumCleanerConsoleButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner", name="Vacuum Cleaner")

    def tearDown(self):
        self.selenium.quit()

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

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## CONSOLE
        console = self.selenium.find_element(By.ID, "console_button")
        console.click()


class TestVacuumCleanerSaveButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner", name="Vacuum Cleaner")


    def tearDown(self):
        self.selenium.quit()

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

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## SAVE BUTTON
        save_button = self.selenium.find_element(By.ID, "save")
        save_button.click()


class TestVacuumCleanerGazeboButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner", name="Vacuum Cleaner")


    def tearDown(self):
        self.selenium.quit()

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

        ## ENTER & CLOSE MODAL
        element = self.selenium.find_element(By.XPATH,
            f'//a[@href="/academy/exercise/{self.exercise.exercise_id}"]/./..')
        element.click()
        ActionChains(self.selenium).move_by_offset(200, 100).click().perform()

        time.sleep(2)
        ## GAZEBO BUTTON
        gazebo_button = self.selenium.find_element(By.ID, "gazebo_button")
        gazebo_button.click()


class TestVacuumCleanerEfficacyButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner", name="Vacuum Cleaner")


    def tearDown(self):
        self.selenium.quit()

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

        ## ENTER & CLOSE MODAL
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


class TestVacuumCleanerLocLaunchButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner_loc", name="Localized Vacuum Cleaner")


    def tearDown(self):
        self.selenium.quit()

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


class TestVacuumCleanerLocTheoryButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner_loc", name="Localized Vacuum Cleaner")

    def tearDown(self):
        self.selenium.quit()

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


class TestVacuumCleanerLocForumButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner_loc", name="Localized Vacuum Cleaner")

    def tearDown(self):
        self.selenium.quit()

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


class TestVacuumCleanerLocExerciseButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner_loc", name="Localized Vacuum Cleaner")

    def tearDown(self):
        self.selenium.quit()

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


class TestVacuumCleanerLocConsoleButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner_loc", name="Localized Vacuum Cleaner")

    def tearDown(self):
        self.selenium.quit()

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


class TestVacuumCleanerLocSaveButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner_loc", name="Localized Vacuum Cleaner")


    def tearDown(self):
        self.selenium.quit()

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


class TestVacuumCleanerLocGazeboButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner_loc", name="Localized Vacuum Cleaner")


    def tearDown(self):
        self.selenium.quit()

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


class TestVacuumCleanerLocEfficacyButton(LiveServerTestCase):
    def setUp(self):
        opts = Options()
        opts.add_argument(env.str("SELENIUM_DISPLAY", "--headless"))
        if env.str("SELENIUM_BROWSER", "firefox") == "chrome":
            self.selenium = webdriver.Chrome(options=opts)
        else:
            self.selenium = webdriver.Firefox(options=opts)
        self.password = "test1234"
        self.user = create_user(username="testing_user", password=self.password, role="Betatester")
        self.exercise = create_exercise(exercise_id="vacuum_cleaner_loc", name="Localized Vacuum Cleaner")


    def tearDown(self):
        self.selenium.quit()

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
