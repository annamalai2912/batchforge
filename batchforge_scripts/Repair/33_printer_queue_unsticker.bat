@echo off
:: ============================================================
:: PRINTER QUEUE UNSTICKER
:: Kills Print Spooler, deletes all stuck print jobs,
:: restarts the spooler, and re-enables all printers.
:: Run as Administrator.
:: ============================================================
echo === Printer Queue Unsticker ===
echo Stopping Print Spooler...
net stop Spooler >nul
echo.
echo Deleting stuck jobs...
del /f /s /q "%SystemRoot%\System32\spool\PRINTERS\*.*" >nul 2>&1
echo.
echo Restarting Print Spooler...
net start Spooler >nul
echo.
echo Re-enabling offline printers...
powershell -NoProfile -Command ^
  "Get-Printer | Where-Object PrinterStatus -ne 'Normal' | ForEach-Object { ^
    Set-Printer -Name $_.Name -WorkOffline:$false; ^
    Write-Host 'Re-enabled:' $_.Name ^
  }"
echo.
echo Done. All queues cleared at %time%
