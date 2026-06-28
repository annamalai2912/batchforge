@echo off
:: ============================================================
:: USB DEVICE HISTORY LOGGER
:: Queries the Windows registry for every USB device ever
:: plugged in. Great for security auditing.
:: ============================================================
set "OUT=%TEMP%\usb_history.txt"
echo USB Device History Report > "%OUT%"
echo Generated: %date% %time% >> "%OUT%"
echo ========================== >> "%OUT%"
powershell -NoProfile -Command "Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Enum\USBSTOR\*\*' | Select-Object FriendlyName,DeviceType | Format-Table -AutoSize | Out-File '%OUT%' -Append"
echo. >> "%OUT%"
powershell -NoProfile -Command "Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Enum\USB\*\*' | Select-Object FriendlyName,Service | Format-Table | Out-File '%OUT%' -Append"
start notepad "%OUT%"
