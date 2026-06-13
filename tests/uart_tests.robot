*** Settings ***
Library    utils.uart_sim.UARTSimulation    WITH NAME    UART

*** Test Cases ***
UART Echo Test
    UART.Send    HelloBoard
    ${resp}=    UART.Receive
    Should Be Equal    ${resp}    HelloBoard

*** Test Cases ***
UART Error Injection Test
    UART.Enable Error Mode    True
    UART.Send    TestMessage
    ${resp}=    UART.Receive
    Run Keyword If    '${resp}' == 'CORRUPTED'    Log    Received corrupted frame
    Run Keyword If    '${resp}' != 'CORRUPTED'    Should Be Equal    ${resp}    TestMessage
