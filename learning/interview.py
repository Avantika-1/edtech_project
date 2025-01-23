from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.facebook.com/")
driver.maximize_window()
email = driver.find_element(By.ID,"email").send_keys("avantikakumari1995@gmail.com")
password = driver.find_element(By.ID,"pass").send_keys("Sh@urya01")
driver.implicitly_wait(10)
loginbutton= driver.find_element(By.CSS_SELECTOR,"[id='loginbutton']").click()
