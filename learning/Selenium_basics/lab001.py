import time

from selenium import webdriver

def test_open_testalogin():
    driver = webdriver.Edge()
    driver.get("https://preprod.testaonline.com/signin")
    print(driver.title)
    assert driver.title == "Testa | Dev"
    print(driver.session_id)
    time.sleep(10)