@echo off
:: Checks the status of the Windows Firewall profiles.
echo Checking Windows Firewall status...
netsh advfirewall show allprofiles state
pause