@echo off
:: Safely stops Windows Update service and clears the SoftwareDistribution folder (requires Admin).
echo Note: Run as Administrator!
echo Stopping Windows Update service...
net stop wuauserv
echo Clearing update cache...
del /f /q /s %windir%\SoftwareDistribution\Download\*.*
echo Starting Windows Update service...
net start wuauserv
pause