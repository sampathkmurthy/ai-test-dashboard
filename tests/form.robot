*** Settings ***
Resource   ../resources/keywords.robot

*** Test Cases ***
Submit Demo Web Form
    Open Headless Browser    https://www.selenium.dev/selenium/web/web-form.html
    Input Text    name:my-text       John Doe
    Input Text    name:my-password   secret123
    Input Text    name:my-textarea   Hello, this is a test message.
    Click Button  css:button
    Wait Until Page Contains    Received!    timeout=15s
    Page Should Contain         Received!
    Close Browser Session

