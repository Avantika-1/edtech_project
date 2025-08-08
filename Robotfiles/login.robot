# Import files
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${LOGIN_URL}    https://testing.testaonline.com/signin
${BROWSER}      Chrome
${USERNAME}     abhijeet@radiantinfonet.com
${PASSWORD}     123@testing

*** Test Cases ***
Valid Login Test
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Input Text    id=outlined-adornment-email    ${USERNAME}
    Input Text    id=outlined-adornment-password    ${PASSWORD}
    Click Button    xpath=//button[normalize-space()='Login']
    Page Should Contain  xpath=//h1[normalize-space()='Welcome back, Business Dashboard']    Welcome back, Business Dashboard

    [Teardown]    Close Browser

Invalid Login Test
    Open Browser    ${LOGIN_URL}                      ${BROWSER}
    Input Text      id=outlined-adornment-email       ${USERNAME}
    Input Text      id=outlined-adornment-password    wrongpassword
    Click Button    xpath=//button[normalize-space()='Login']
    Page Should Contain                             Invalid username or password
    [Teardown]    Close Browser


