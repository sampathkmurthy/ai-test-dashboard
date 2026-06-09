*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}     https://the-internet.herokuapp.com/login
${BROWSER}    Chrome

*** Keywords ***
Open Login Page
    Open Browser    ${URL}    ${BROWSER}

Enter Username
    [Arguments]    ${username}
    Input Text    id:username    ${username}

Enter Password
    [Arguments]    ${password}
    Input Text    id:password    ${password}

Submit Login
    Click Button    css:button.radius
