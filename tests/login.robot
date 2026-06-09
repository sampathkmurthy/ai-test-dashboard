*** Settings ***
Resource    ../resources/browser_setup.robot

*** Test Cases ***
Valid Login
    Open Headless Browser
    Input Text    id:username    tomsmith
    Input Text    id:password    SuperSecretPassword!
    Wait Until Page Contains    Secure Area    timeout=20s
    Page Should Contain    Secure Area
    Close Browser



