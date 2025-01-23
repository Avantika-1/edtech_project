import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options


def test_open_testalogin():
    driver = webdriver.Edge()
    driver.get("https://preprod.testaonline.com/signin")
    driver.refresh()
    driver.back()
    driver.forward()
    print(driver.page_source)




