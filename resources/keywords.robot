*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${OPTIONS}    add_argument("--headless")

*** Keywords ***
Open Headless Browser
    [Arguments]    ${url}
    Open Browser    ${url}    ${BROWSER}    options=${OPTIONS}

Close Browser Session
    Close Browser

Login With Credentials
    [Arguments]    ${url}    ${username}    ${password}
    Open Headless Browser    ${url}
    Input Text    id:username    ${username}
    Input Text    id:password    ${password}
    Click Button    css:button.radius
    Page Should Contain    Secure Area
    Close Browser Session
