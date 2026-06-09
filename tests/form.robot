*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/keywords.robot

*** Test Cases ***
Submit Forgot Password Form
    Open Headless Browser    https://the-internet.herokuapp.com/forgot_password
    Input Text    id:email    johndoe@example.com
    Click Button    css:button.radius
    Wait Until Page Contains Element    css:h1    timeout=20s
    ${text}=    Get Text    css:h1
    Run Keyword If    '${text}' == 'Your e-mail\'s been sent!'    Log    Success message appeared
    ...    ELSE    Log    Forgot password form returned error: ${text}
    Close Browser Session    
