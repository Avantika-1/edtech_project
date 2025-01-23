from appium.webdriver.webdriver import AppiumOptions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium import webdriver

appium_options = AppiumOptions()
appium_options.load_capabilities({
     "platformName": "Android",
     "appium:deviceName": "Redmi A2",
     "appium:app": "C:\\Users\\Admin\\Downloads\\application-959e753a-becd-4bc8-a76a-84a587dec56a.apk",
})

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=appium_options)
driver.implicitly_wait(20)
driver.find_element('xpath','//android.view.ViewGroup[@content-desc="हिन्दी, Hindi"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="पुष्टि करें"]').click()
driver.implicitly_wait(10)
#Navigate to Home page

driver.find_element('id', 'android:id/content')


#click on Login button of homepage

driver.find_element('xpath','//android.widget.Button[@content-desc="लॉग इन करें"]').click()
driver.implicitly_wait(10)

#Navigate to Login page
driver.find_element('xpath','(//android.widget.EditText[@resource-id="text-input-outlined"])[1]')
driver.find_element('xpath','(//android.widget.EditText[@resource-id="text-input-outlined"])[1]').send_keys("avantika@radiantinfonet.com")
driver.find_element('xpath','(//android.widget.EditText[@resource-id="text-input-outlined"])[2]').click()
driver.find_element('xpath','(//android.widget.EditText[@resource-id="text-input-outlined"])[2]').send_keys("Test@123")
driver.implicitly_wait(5)
driver.find_element('xpath','//android.widget.Button[@content-desc="लॉग इन करें"]').click()
driver.implicitly_wait(20)

#Navigate to Upcoming Batch Screen
driver.find_element('xpath','//android.view.View[@content-desc="बैचेस"]').click()
driver.implicitly_wait(10)
driver.find_element('xpath','//android.widget.TextView[@text="आगामी"]')
driver.implicitly_wait(10)
#Navigate to Ongoing Batch Screen
driver.find_element('xpath','//android.widget.TextView[@text="चल रहा है"]').click()
driver.implicitly_wait(10)

driver.find_element('xpath','//android.widget.TextView[@text="बैच आईडी[0]"]').click()

#Navigate to Ongoing Batch Screen
driver.find_element('xpath','//android.widget.TextView[@text="चल रहा है"]').click()
driver.implicitly_wait(10)

driver.find_element('xpath','//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup').click()
driver.implicitly_wait(10)
driver.find_element('xpath','//android.widget.TextView[@text="बैच आईडी : Apptestbatch"]').click()
driver.find_element('xpath','//android.widget.TextView[@text="बैच लंबित"]').click()

#Clock in
driver.find_element('xpath','//android.widget.TextView[@resource-id="button-text"]')
driver.implicitly_wait(40)
driver.find_element('xpath','//android.widget.TextView[@resource-id="button-text"]').click()





