from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


def test_signin():
        service = Service(executable_path='C:\Program Files\Driver\chromedriver-win64\chromedriver.exe')
        driver= webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get("https://testing.testaonline.com/signin")

        email_id = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-email"))
        )
        email_id.send_keys("zaakefsotysvlrkopb@ckptr.com")

        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-password"))
        )
        password.send_keys("SuperAdmin@1234")

        signin_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Login']"))

        )
        signin_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Welcome back, Business Dashboard']"))
        )

        print("Signin Successful!")


test_signin()
