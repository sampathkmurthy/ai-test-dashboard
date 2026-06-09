*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/keywords.robot

*** Test Cases ***
Submit Forgot Password Form
    Open Headless Browser    https://the-internet.herokuapp.com/forgot_password
    Input Text    id:email    johndoe@example.com
    Click Button  css:button.radius
    Wait Until Page Contains Element    css:h1    timeout=30s
    Element Text Should Be    css:h1    Your e-mail's been sent!
    Close Browser Session    
