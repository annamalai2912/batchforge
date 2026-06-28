@echo off
setlocal enabledelayedexpansion
:: ============================================================
:: WI-FI PASSWORD EXTRACTOR
:: Dumps all saved Wi-Fi profile names and plaintext passwords
:: from Windows Credential Store.
:: ============================================================
set "OUT=%USERPROFILE%\Desktop\wifi_passwords.txt"
echo Wi-Fi Password Export > "%OUT%"
echo Generated: %date% %time% >> "%OUT%"
echo ======================== >> "%OUT%"
for /f "skip=9 tokens=2 delims=:" %%S in ('netsh wlan show profiles') do (
    set "SSID=%%S"
    set "SSID=!SSID:~1!"
    echo. >> "%OUT%"
    echo SSID: !SSID! >> "%OUT%"
    netsh wlan show profile name="!SSID!" key=clear 2>nul | findstr "Key Content" >> "%OUT%"
)
echo Saved: %OUT%
type "%OUT%"
