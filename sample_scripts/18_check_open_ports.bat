@echo off
:: Lists all listening ports on the system.
echo Checking open ports...
netstat -an | find "LISTEN"
pause