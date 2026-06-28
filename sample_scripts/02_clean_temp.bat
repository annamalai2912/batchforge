@echo off
echo =========================
echo Cleaning Temporary Files
echo =========================
del /q /f /s %TEMP%\*
del /q /f /s C:\Windows\Temp\*
echo Cleanup Complete!
pause
