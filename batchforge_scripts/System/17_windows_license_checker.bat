@echo off
:: ============================================================
:: WINDOWS ACTIVATION AND LICENSE CHECKER
:: Reads product key, checks activation status, OEM/Retail.
:: ============================================================
echo Windows License Report
echo ======================
echo.
echo Activation Status:
cscript //nologo "%SystemRoot%\System32\slmgr.vbs" /dli
echo.
echo Extended License Info:
cscript //nologo "%SystemRoot%\System32\slmgr.vbs" /dlv
echo.
echo OEM Key (if available):
powershell -NoProfile -Command ^
  "(Get-WmiObject -query 'select * from SoftwareLicensingService').OA3xOriginalProductKey" 2>nul
pause
