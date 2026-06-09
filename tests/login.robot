*** Settings ***
Library    SeleniumLibrary
Resource   ../page_objects/login_page.robot

*** Test Cases ***

Valid Login
    Open Browser    https://the-internet.herokuapp.com/login    chrome    options=add_argument("--headless")
    Input Text    id:username    tomsmith
    Input Text    id:password    SuperSecretPassword!
    Click Button    css:button.radius
    Page Should Contain    Secure Area
    Close Browser


