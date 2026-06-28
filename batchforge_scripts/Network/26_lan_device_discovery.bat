@echo off
:: ============================================================
:: LAN DEVICE DISCOVERY SCANNER
:: ARP-pings the entire local /24 subnet, resolves hostnames,
:: and lists every live device with IP and MAC address.
:: Edit SUBNET to match your network (e.g. 192.168.0)
:: ============================================================
echo LAN Device Discovery
echo ====================
set "SUBNET=192.168.1"
set "OUT=%TEMP%\lan_devices.txt"
echo Pinging %SUBNET%.1 - %SUBNET%.254...
for /l %%i in (1,1,254) do (
    start /b ping -n 1 -w 200 %SUBNET%.%%i >nul 2>&1
)
timeout /t 3 /nobreak >nul
echo.
echo Live devices:
arp -a | findstr /v "Interface" | findstr /v "^$" | findstr "%SUBNET%"
arp -a > "%OUT%"
echo Full ARP table saved: %OUT%
