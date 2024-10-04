import pytest
from appium.webdriver.webdriver import AppiumOptions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver


@pytest.fixture(scope='module')
def driver():
    appium_options = AppiumOptions()
    appium_options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "emulator-5556",
        "appium:app": "C:\\Users\\Admin\\Downloads\\application-959e753a-becd-4bc8-a76a-84a587dec56a.apk",
    })

    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=appium_options)
    yield driver
    driver.quit()


def test_login(driver):
    wait = WebDriverWait(driver, 20)

    # Select language
    wait.until(EC.element_to_be_clickable(('xpath', '//android.view.ViewGroup[@content-desc="हिन्दी, Hindi"]'))).click()
    wait.until(EC.element_to_be_clickable(('xpath', '//android.widget.Button[@content-desc="पुष्टि करें"]'))).click()

    # Navigate to Home page
    wait.until(EC.element_to_be_clickable(('xpath', '//android.widget.FrameLayout[@resource-id="android:id/content"]//android.view.ViewGroup'))).click()

    # Login into assessor app
    email_input = wait.until(EC.visibility_of_element_located(('xpath', '(//android.widget.EditText[@resource-id="text-input-outlined"])[1]')))
    email_input.click()
    email_input.send_keys("avantika@radiantinfonet.com")

    password_input = wait.until(EC.visibility_of_element_located(('xpath', '(//android.widget.EditText[@resource-id="text-input-outlined"])[2]')))
    password_input.click()
    password_input.send_keys("Test@123")

    wait.until(EC.element_to_be_clickable(('xpath', '//android.widget.Button[@content-desc="लॉग इन करें"]'))).click()

    # Optionally, you could add assertions here to verify login success
