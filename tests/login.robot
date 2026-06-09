*** Settings ***
Resource    ../resources/browser_setup.robot

*** Test Cases ***
Valid Login
    Open Headless Browser
    Input Text    id:username    tomsmith
    Input Text    id:password    SuperSecretPassword!
    Click Button    css:button.radius
    Wait Until Page Contains Element    css:div.flash.success    timeout=30s
    Page Should Contain    Secure Area
    Close Browser



