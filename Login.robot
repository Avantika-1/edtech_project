*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://testing.testaonline.com/signin
${BROWSER}    Chrome
${DRIVER_PATH}    C:\Program Files\Driver\chromedriver-win64\chromedriver.exe
${USERNAME}    zaakefsotysvlrkopb@ckptr.com
${PASSWORD}    SuperAdmin@1234

*** Test Cases ***
Test Signin
    Open Browser    ${URL}    ${BROWSER}    executable_path=${DRIVER_PATH}
    Maximize Browser Window
    Input Text    id=outlined-adornment-email    ${USERNAME}
    Input Text    id=outlined-adornment-password    ${PASSWORD}
    Click Button    xpath=//button[normalize-space()='Login']
    Wait Until Element Is Visible    xpath=//h1[normalize-space()='Welcome back, Business Dashboard']
    Log    Signin Successful!
    Close Browser
