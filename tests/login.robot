*** Settings ***
Resource    ../resources/keywords.robot

*** Variables ***
${BROWSER}          chrome
${OPTIONS}          add_argument("--headless")
${RETRY_ATTEMPTS}   3
${RETRY_DELAY}      2s

*** Keywords ***
Open Headless Browser
    [Arguments]    ${url}
    Open Browser    ${url}    ${BROWSER}    options=${OPTIONS}

Close Browser Session
    Close Browser

Retry Keyword
    [Arguments]    ${keyword}    @{args}
    FOR    ${i}    IN RANGE    ${RETRY_ATTEMPTS}
        Log    Attempt ${i+1} for keyword: ${keyword} with args: ${args}
        ${result}=    Run Keyword And Ignore Error    ${keyword}    @{args}
        Run Keyword If    '${result[0]}' == 'PASS'    Exit For Loop
        Sleep    ${RETRY_DELAY}
    END
    Run Keyword If    '${result[0]}' == 'FAIL'    Fail    Keyword ${keyword} failed after ${RETRY_ATTEMPTS} attempts

Login With Credentials (Retry)
    [Arguments]    ${url}    ${username}    ${password}    ${expected}
    Open Headless Browser    ${url}
    Retry Keyword    Input Text    id:username    ${username}
    Retry Keyword    Input Text    id:password    ${password}
    Retry Keyword    Click Button    css:button.radius
    Wait Until Page Contains    ${expected}    timeout=10s
    Page Should Contain    ${expected}
    Close Browser Session

*** Test Cases ***
Valid Login With Retry
    Login With Credentials (Retry)    https://the-internet.herokuapp.com/login    tomsmith    SuperSecretPassword!    Secure Area

Invalid Login With Retry
    Login With Credentials (Retry)    https://the-internet.herokuapp.com/login    wronguser    wrongpassword    Your username is invalid!
