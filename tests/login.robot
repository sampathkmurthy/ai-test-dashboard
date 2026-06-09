*** Settings ***
Library    SeleniumLibrary
Resource   ../page_objects/login_page.robot

*** Test Cases ***
Valid Login
    Open Login Page
    Enter Username    tomsmith
    Enter Password    SuperSecretPassword!
    Submit Login
    Page Should Contain    Secure Area
    Close Browser


