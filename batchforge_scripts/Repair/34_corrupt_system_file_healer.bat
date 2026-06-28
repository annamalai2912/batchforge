@echo off
:: ============================================================
:: CORRUPT SYSTEM FILE HEALER
:: Runs SFC /scannow then DISM RestoreHealth sequentially.
:: Highlights repaired or unrepairable files in output.
:: Run as Administrator.
:: ============================================================
set "LOG=%TEMP%\sfc_dism_report.txt"
echo System File Healer > "%LOG%"
echo Started: %date% %time% >> "%LOG%"
echo ======================== >> "%LOG%"
echo.
echo [1/2] Running SFC /scannow (may take 5-10 mins)...
sfc /scannow >> "%LOG%" 2>&1
echo.
echo [2/2] Running DISM RestoreHealth...
DISM /Online /Cleanup-Image /RestoreHealth >> "%LOG%" 2>&1
echo.
echo Scan complete at %time%
type "%LOG%" | findstr /i "repaired found integrity corrupt"
echo.
echo Full report: %LOG%
pause
