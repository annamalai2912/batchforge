@echo off
echo =========================
echo Checking Internet Connection
echo =========================
ping 8.8.8.8 -n 4
if %errorlevel% == 0 (
    echo.
    echo Status: Internet is CONNECTED.
) else (
    echo.
    echo Status: Internet is DISCONNECTED.
)
pause
