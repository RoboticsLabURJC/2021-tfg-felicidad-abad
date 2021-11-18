from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = r"C:\Users\cafiz\OneDrive\Documentos\Universidad\TFG\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.es/")
print(driver.title)

## Aceptar el popup
aceptar = driver.find_element_by_id("L2AGLb")
aceptar.click()

time.sleep(10)
driver.quit()
