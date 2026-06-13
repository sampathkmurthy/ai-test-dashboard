*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${OPTIONS}    add_argument("--headless")

*** Keywords ***
Open Headless Browser
    [Arguments]    ${url}
    Open Browser    ${url}    ${BROWSER}    options=${OPTIONS}

Close Browser Session
    Close Browser

Retry Keyword
    [Arguments]    ${keyword}    @{args}
    FOR    ${i}    IN RANGE    3
        Log    Attempt ${i+1} for keyword: ${keyword} with args: ${args}
        ${result}=    Run Keyword And Ignore Error    ${keyword}    @{args}
        Run Keyword If    '${result[0]}' == 'PASS'    Exit For Loop
        Sleep    2s
    END
    Run Keyword If    '${result[0]}' == 'FAIL'    Fail    Keyword ${keyword} failed after 3 attempts

Login With Credentials (Retry)
    [Arguments]    ${url}    ${username}    ${password}
    Open Headless Browser    ${url}
    Retry Keyword    Input Text    id:username    ${username}
    Retry Keyword    Input Text    id:password    ${password}
    Retry Keyword    Click Button    css:button.radius
    Page Should Contain    Secure Area
    Close Browser Session
