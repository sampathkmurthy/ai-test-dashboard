*** Settings ***
Library    utils.gpio_sim.GPIOSimulation    WITH NAME    GPIO
Library    Collections

*** Test Cases ***
Toggle GPIO Pin
    GPIO.Set High    5
    ${state}=    GPIO.Read State    5
    Should Be Equal As Integers    ${state}    1
    GPIO.Set Low    5
    ${state}=    GPIO.Read State    5
    Should Be Equal As Integers    ${state}    0

GPIO Interrupt Test
    ${events}=    Create List
    GPIO.Register Interrupt    5    Keyword Callback    ${events}    debounce_ms=200    edge=both
    GPIO.Set High    5
    GPIO.Set Low     5
    Sleep    0.2s    # allow async callback
    Should Not Be Empty    ${events}

GPIO Interrupt With Debounce
    ${events}=    Create List
    GPIO.Register Interrupt    5    Keyword Callback    ${events}    debounce_ms=200    edge=both
    GPIO.Set High    5
    Sleep    0.05s
    GPIO.Set Low     5
    Sleep    0.05s
    GPIO.Set High    5
    Sleep    0.05s
    Sleep    0.2s    # wait for callback
    Length Should Be    ${events}    1
    Should Contain    ${events[0]}    Pin 5 State 1

*** Keywords ***
Keyword Callback
    [Arguments]    ${events}    ${pin}    ${state}
    Append To List    ${events}    Pin ${pin} State ${state}
