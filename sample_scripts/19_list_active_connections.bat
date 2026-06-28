@echo off
:: Lists established network connections.
echo Listing active connections...
netstat -an | find "ESTABLISHED"
pause