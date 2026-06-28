@echo off
:: Restarts the Windows Explorer process safely.
echo Restarting Windows Explorer...
taskkill /f /im explorer.exe
start explorer.exe
echo Explorer restarted.
pause