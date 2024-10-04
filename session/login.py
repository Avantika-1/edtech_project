import appium import webdriver

"""
Desired Capablities 
"""

desired_cap={
    "platformName": "Android",
    "appium:platformVersion": "11",
    "appium:deviceName": "Pixel 8a",
    "appium:automationName": "UIAutomator2",
    "appium:app": "C:\\Users\\Admin\\Downloads\\application-959e753a-becd-4bc8-a76a-84a587dec56a.apk",
    "appium:avd": "Pixel_8a_API_35",
    "uiautomator2ServerLaunchTimeout": 90000
    "appPackage":""
    "appWaitActivity":""
}

webdriver.Remote("")