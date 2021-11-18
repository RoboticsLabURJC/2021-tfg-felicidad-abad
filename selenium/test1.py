from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = r"C:\Users\cafiz\OneDrive\Documentos\Universidad\TFG\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.es/")
print(driver.title)

driver.quit()
