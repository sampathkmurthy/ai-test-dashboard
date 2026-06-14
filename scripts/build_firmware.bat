@echo off
call "C:\Program Files\Microsoft Visual Studio\18\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
cl firmware\firmware.c firmware\hal_spi.c ws2_32.lib /Fe:firmware.exe
