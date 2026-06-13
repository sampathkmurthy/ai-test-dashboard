*** Settings ***
Library    utils.uart_sim.UARTSimulation    WITH NAME    UART

*** Test Cases ***
UART Echo Test
    UART.Send    HelloBoard
    ${resp}=    UART.Receive    timeout_ms=500
    Should Be Equal    ${resp}    HelloBoard

Deterministic UART Seed
    UART.Set Seed    42
    UART.Enable Error Mode    True    1.0
    UART.Send    TestMsg
    ${resp}=    UART.Receive    timeout_ms=500
    Should Be Equal    ${resp}    CORRUPTED

UART Timeout And Delay
    UART.Set Seed    1
    UART.Enable Error Mode    False
    UART.Set Delay    500
    UART.Send    SlowMsg
    ${resp}=    UART.Receive    timeout_ms=100
    Should Be Equal    ${resp}    ${EMPTY}
    ${resp}=    UART.Receive    timeout_ms=1000
    Should Be Equal    ${resp}    SlowMsg

UART Error Injection Probability
    UART.Set Seed    123
    UART.Enable Error Mode    True    1.0
    UART.Send    DataFrame
    ${resp}=    UART.Receive    timeout_ms=500
    Should Be Equal    ${resp}    CORRUPTED

