@echo off
setlocal enabledelayedexpansion
set "PORT=65432"
set "PYTHON=%~dp0..\venv\Scripts\python.exe"
set "SCRIPT=%~dp0run_spi_server.py"

rem If the port is already listening, assume the SPI server is already running.
netstat -ano | findstr /R /C:":%PORT% .*LISTENING" >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo SPI server already running on port %PORT%.
    exit /b 0
)

rem Launch the SPI server detached so the task sequence continues.
start "SPI Server" /b "%PYTHON%" "%SCRIPT%"
echo SPI server launched in background on port %PORT%.
endlocal
