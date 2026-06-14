*** Settings ***
Library    utils.sensor_sim.TempSensorSimulation    WITH NAME    Sensor

*** Test Cases ***
Sensor Normal Read
    ${val}=    Sensor.Read Value
    Should Be True    ${val} >= 24.5 and ${val} <= 25.5

Sensor Error Injection
    Sensor.Enable Error Mode    True
    ${val}=    Sensor.Read Value
    Run Keyword If    '${val}' == 'CRC_ERROR'    Log    Simulated CRC error detected
    Run Keyword If    '${val}' != 'CRC_ERROR'    Should Be True    ${val} >= 24.0 and ${val} <= 26.0

Sensor Deterministic Seed
    Sensor.Set Seed    123
    ${val1}=    Sensor.Read Value
    Sensor.Set Seed    123
    ${val2}=    Sensor.Read Value
    Should Be Equal    ${val1}    ${val2}
