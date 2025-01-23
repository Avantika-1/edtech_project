import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure



def test_open_testalogin():
    driver = webdriver.Edge()
    driver.get("https://preprod.testaonline.com/signin")
    email = driver.find_element(By.CSS_SELECTOR, "[type='email']")
    email.send_keys("abhijeet@radiantinfonet.com")
    email = driver.find_element(By.NAME, "password")
    email.send_keys("Abhijeet@123")
    time.sleep(100)


def test_open_testalogin_Invalidcred():
    driver = webdriver.Edge()
    driver.get("https://preprod.testaonline.com/signin")
    email = driver.find_element(By.CSS_SELECTOR, "[type='email']")
    email.send_keys("abhijeet@radiantinfonet.com")
    email = driver.find_element(By.NAME, "password")
    email.send_keys("Abhijeet@12")
    time.sleep(100)
    errormsz = driver.find_element(By.CLASS_NAME,"error-box")
    assert errormsz.text == "wrong password"
    time.sleep(100)

    #Link_text = exact match
    #partial link text = partial match
    #absolute Xpath - whole node
    #disadvntage :-> too big, if any attribute change whole code wnet

