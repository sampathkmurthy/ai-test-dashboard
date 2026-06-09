*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/keywords.robot

*** Test Cases ***
Submit Forgot Password Form
    Open Headless Browser    https://the-internet.herokuapp.com/forgot_password
    Input Text    id:email    johndoe@example.com
    Click Button  css:button.radius
    Wait Until Page Contains    Your e-mail's been sent!    timeout=10s
    Page Should Contain    Your e-mail's been sent!
    Close Browser Session    
