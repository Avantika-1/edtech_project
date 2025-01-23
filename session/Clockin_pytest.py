import pytest
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Define a pytest fixture to set up the Appium driver
@pytest.fixture(scope='module')
def appium_driver():
    appium_options = AppiumOptions()
    appium_options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "Redmi A2",
        "appium:app": "C:\\Users\\Admin\\Downloads\\application-959e753a-becd-4bc8-a76a-84a587dec56a.apk",
    })

    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=appium_options)
    driver.implicitly_wait(20)  # Set an implicit wait time

    yield driver  # Provide the driver to the test functions

    driver.quit()  # Teardown: Close the driver after the tests


# Test to navigate through the app and login
def test_app_navigation_and_login(appium_driver):
    driver = appium_driver

    # Select Hindi language
    driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="हिन्दी, Hindi"]').click()

    # Confirm selection
    driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="पुष्टि करें"]').click()
    driver.implicitly_wait(10)

    # Click on Login button of the homepage
    driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="लॉग इन करें"]').click()

    # Wait until login page loads
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '(//android.widget.EditText[@resource-id="text-input-outlined"])[1]'))
    )

    # Enter email and password
    email_input = driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="text-input-outlined"])[1]')
    email_input.send_keys("avantika@radiantinfonet.com")

    password_input = driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="text-input-outlined"])[2]')
    password_input.click()
    password_input.send_keys("Test@123")

    # Click on the login button
    driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="लॉग इन करें"]').click()

    driver.implicitly_wait(20)  # Wait for login process

    # Verify login success by checking the presence of the "Batch" screen element
    assert driver.find_element(By.XPATH, '//android.view.View[@content-desc="बैचेस"]')


# Test to navigate through batches and clock in
def test_navigate_batches_and_clock_in(appium_driver):
    driver = appium_driver

    # Navigate to Upcoming Batch screen
    driver.find_element(By.XPATH, '//android.view.View[@content-desc="बैचेस"]').click()
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, '//android.widget.TextView[@text="आगामी"]').click()  # Upcoming
    driver.implicitly_wait(10)

    # Navigate to Ongoing Batch Screen
    driver.find_element(By.XPATH, '//android.widget.TextView[@text="चल रहा है"]').click()  # Ongoing
    driver.implicitly_wait(10)

    # Select a specific batch by ID


    # Click on an element to open batch details
    driver.find_element(By.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup').click()
    driver.implicitly_wait(10)

    # Select batch "Apptestbatch" (or modify as per your test batch name)
    driver.find_element(By.XPATH, '//android.widget.TextView[@text="बैच आईडी : Apptestbatch"]').click()

    # Check for "Batch Pending" status and clock in
    driver.find_element(By.XPATH, '//android.widget.TextView[@text="बैच लंबित"]').click()

    # Wait for the Clock In button to appear and then click
    clock_in_btn = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="button-text"]')
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable(clock_in_btn))
    clock_in_btn.click()

