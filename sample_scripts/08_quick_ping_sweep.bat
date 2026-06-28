@echo off
echo =========================
echo Subnet Ping Sweep (192.168.1.x)
echo =========================
echo This may take a moment...
for /L %%i in (1,1,254) do (
    ping -n 1 -w 100 192.168.1.%%i >nul
    if not errorlevel 1 echo 192.168.1.%%i is UP
)
echo Sweep complete.
pause
