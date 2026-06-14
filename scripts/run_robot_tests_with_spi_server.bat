@echo off
setlocal
set "ROOT=%~dp0.."
call "%~dp0start_spi_server.bat"
if errorlevel 1 exit /b 1
"%ROOT%\venv\Scripts\python.exe" -m robot "%ROOT%\tests"
endlocal
