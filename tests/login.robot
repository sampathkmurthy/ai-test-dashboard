
*** Settings ***
Resource    ../resources/browser_setup.robot
#Library     utils.selenium_keywords

*** Test Cases ***
Valid Login
    Open Headless Browser
    Input Text    id=username    tomsmith
    Input Text    id=password    SuperSecretPassword!
    Click Button    xpath=//button[@type='submit']
    Wait Until Page Contains Element    css:div.flash.success    timeout=30s
    Page Should Contain    Secure Area
    Close Browser



