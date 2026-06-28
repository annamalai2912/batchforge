@echo off
:: Runs basic network troubleshooting commands.
echo Pinging Google DNS...
ping 8.8.8.8
echo.
echo Tracing route to Google DNS...
tracert -d -h 5 8.8.8.8
pause