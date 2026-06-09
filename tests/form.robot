*** Settings ***
Library    SeleniumLibrary
Resource   ../keywords.robot

*** Test Cases ***
Submit Contact Form Successfully
    Open Headless Browser    https://the-internet.herokuapp.com/contact-us
    Input Text    id:name    John Doe
    Input Text    id:email   johndoe@example.com
    Input Text    id:message Hello, this is a test message.
    Click Button  css:button[type="submit"]
    Wait Until Page Contains Element    css:div.flash.success    timeout=20s
    Page Should Contain    Thank You
    Close Browser Session

Submit Contact Form With Invalid Email
    Open Headless Browser    https://the-internet.herokuapp.com/contact-us
    Input Text    id:name    Jane Doe
    Input Text    id:email   not-an-email
    Input Text    id:message Testing invalid email case.
    Click Button  css:button[type="submit"]
    Wait Until Page Contains Element    css:div.flash.error    timeout=20s
    Page Should Contain    Invalid email address
    Close Browser Session
