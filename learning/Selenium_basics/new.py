import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options


driver = webdriver.Edge()
new_x = driver.find_element(By.XPATH,"//button[text()="Login"]")
new_x.send_keys("")

#https://www.youtube.com/watch?v=MMymYTFV3Cs&ab_channel=AutomationRail
