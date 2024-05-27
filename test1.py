from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_signin():
    service = Service(executable_path='C:\Program Files\Driver\chromedriver-win64\chromedriver.exe')
    driver=webdriver.Chrome(service=service)
     '''
    driver = webdriver.Chrome()
    driver.maximize_window()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    '''


    driver.get("https://testing.testaonline.com/signin")

    try:

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

        driver.get("https://testing.testaonline.com/exam-management/create-batch")

    finally:

        test_signin()
