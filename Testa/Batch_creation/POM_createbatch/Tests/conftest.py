import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():


    """Setup and teardown for WebDriver."""
    driver = webdriver.Edge()

   # service = Service(ChromeDriverManager().install())
   # driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    yield driver  # Pass driver instance to test

    driver.quit()  # Teardown


@pytest.fixture(scope="function")
def login(driver):

    driver.get("https://preprod.testaonline.com/signin")


    Email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys("abhijeet@radiantinfonet.com")

    driver.find_element(By.NAME, "password").send_keys("Abhijeet@123")

    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome')]"))
    )

    yield driver
