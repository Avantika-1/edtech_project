# a tag :> anchor tag which use to give user a hyper link
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


@Alluredescription(Verify navigating to admin navigation url)
def test_open_testalogin():
    driver = webdriver.Edge()
    driver.get("https://preprod.testaonline.com/")
    Go_toSignIn = driver.find_element(By.TAG_NAME, "a")
    Go_toSignIn.click()
    time.sleep(30)
    # verify URL change

    assert driver.current_url == "https://preprod.testaonline.com/signin"


