import pytest
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


@pytest.fixture(scope="module")
def appium_driver():
    # Set up desired capabilities
    desired_capabilities = {

        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:deviceName": "Redmi A2",
        "appium:automationName": "UIAutomator2",
        "appium:app": "C:\\Users\\Admin\\Downloads\\application-959e753a-becd-4bc8-a76a-84a587dec56a.apk",
        "appium:uiautomator2ServerLaunchTimeout": 90000,
        "appium:udid": "CYKJWO8XEMAEZXKJ"
    }

    # Initialize the Appium driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    yield driver
    driver.quit()

    user_action = TouchAction(driver)
def click_allow_button(driver, com=None):
    try:
        # Wait for the popup to appear
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('xpath', "//android.widget.FrameLayout[@resource-id="android:id/content"]/"android.widget.FrameLayout")))

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('xpath'," //android.widget.LinearLayout[@resource-id="com.android.permissioncontroller:id/content_container"]/android.widget.LinearLayout")))


        # Locate the Allow button
        allow_button = driver.find_element('xpath',"//android.widget.Button[@resource-id="com.android.permissioncontroller":id/permission_allow_button]")

        user_action.tap(allow_button)

        # Optionally verify that the button was clicked
        print("Clicked on Allow button.")

    except TimeoutException:
        print("Popup did not appear in time.")
    except NoSuchElementException:
        print("Allow button not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def test_select_language(driver):
    driver = appium_driver
    sleep(2)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('xpath', "//android.widget.ScrollView")))

    # Locate the English language widget
    English_widget = driver.find_element('xpath',//android.view.ViewGroup[@content-desc="English, English"])
    English_widget.click()

    # Optionally verify that the button was clicked
    print("English Language selected")

    # Click the Allow button on the popup
    test_select_language(driver)
def test_click_confirmlang_button(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('xpath', "//android.widget.ScrollView")))

    # Locate the Confirm button
    Confirm_button = driver.find_element('xpath', "//android.widget.TextView[@resource-id="button-text"]")
    Confirm_button.click()

    # Optionally verify that the button was clicked
    print("English Language selected & submitted sucessfully")

    # Click the Allow button on the popup
    test_click_submit_button(driver)


