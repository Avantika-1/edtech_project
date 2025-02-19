*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${LOGIN_URL}       https://preprod.testaonline.com/signin
${BROWSER}         Chrome
${EMAIL}           abhijeet@radiantinfonet.com
${PASSWORD}        Abhijeet@123
${USERNAME_FIELD}  id=outlined-adornment-email
${PASSWORD_FIELD}  id=outlined-adornment-password
${LOGIN_BUTTON}    xpath=//button[normalize-space()='Login']

*** Test Cases ***
User Should Be Able To Login
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Input Text      ${USERNAME_FIELD}    ${EMAIL}
    Input Text      ${PASSWORD_FIELD}    ${PASSWORD}
    Click Button    ${LOGIN_BUTTON}
    Wait Until Page Contains    Dashboard    timeout=5s
    Capture Page Screenshot
    Close Browser



*** Keywords ***
