from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from environs import Env
from selenium.webdriver.common.action_chains import ActionChains

env = Env()
env.read_env()

try:
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get(env("UNIBOTICS_URL"))
    print(driver.title)

    buttons = driver.find_elements(By.CLASS_NAME, "page-scroll")
    log_in_button = buttons[2]
    log_in_button.click()

    time.sleep(10)
    username = driver.find_element(By.NAME,"username")
    username.send_keys(env("UNIBOTICS_USER"))

    password = driver.find_element(By.NAME, "password")
    password.send_keys(env("UNIBOTICS_PASS"))

    enter = driver.find_element(By.XPATH, "//input[@class='fadeIn fourth']")
    enter.click()

    time.sleep(10)

    ## ENTER COLOR FILTER & CLOSE MODAL
    go_to_exercise = env("UNIBOTICS_URL") + "academy/exercise/color_filter"
    driver.get(go_to_exercise)

    ActionChains(driver).move_by_offset(200, 100).click().perform()

    ## FORUM
    console = driver.find_element(By.ID, "open-forum")
    console.click()

    click_console = driver.find_element(By.ID, "open-exercise")
    click_console.click()

except:
    print("El test ha fallado")

time.sleep(10)
driver.quit()
