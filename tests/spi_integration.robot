*** Settings ***
Library    api/spi_api.py

*** Test Cases ***
Valid Sensor Frame
    [Documentation]    Verify firmware returns a valid temperature frame with CRC_OK
    ${output}=    Run Firmware    READ_TEMP
    Should Contain    ${output}    CRC_OK
    Should Contain    ${output}    TEMP:25.13

CRC Error Frame
    [Documentation]    Verify firmware detects CRC error in sensor frame
    ${output}=    Run Firmware    READ_FAULT
    Should Contain    ${output}    CRC_ERROR
    Should Contain    ${output}    TEMP:xx.xx

Unknown Command Frame
    [Documentation]    Verify firmware handles unknown SPI command gracefully
    ${output}=    Run Firmware    INVALID_CMD
    Should Contain    ${output}    UNKNOWN_COMMAND

