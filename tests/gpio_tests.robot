*** Settings ***
Library    utils.gpio_sim.GPIOSimulation    WITH NAME    GPIO
Library    utils.uart_sim.UARTSimulation    WITH NAME    UART

*** Test Cases ***
Toggle GPIO Pin
    GPIO.Set High    5
    ${state}=    GPIO.Read State    5
    Should Be Equal As Integers    ${state}    1
    GPIO.Set Low    5
    ${state}=    GPIO.Read State    5
    Should Be Equal As Integers    ${state}    0

GPIO Interrupt Test
    GPIO.Register Interrupt    5    Log Pin Change
    GPIO.Set High    5
    GPIO.Set Low     5

UART Echo Test
    UART.Send    HelloBoard
    ${resp}=    UART.Receive
    Should Be Equal    ${resp}    HelloBoard

*** Keywords ***
Log Pin Change
    [Arguments]    ${pin}    ${state}
    Log    Interrupt: Pin ${pin} changed to ${state}    
