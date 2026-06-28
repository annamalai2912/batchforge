@echo off
:: ============================================================
:: BANDWIDTH USAGE LOGGER PER PROCESS
:: Logs top network-connected processes every 30 seconds.
:: Shows PID, name, and active connection count.
:: ============================================================
set "LOG=%TEMP%\bandwidth_log.txt"
echo Bandwidth Monitor - %date% > "%LOG%"
echo ============================== >> "%LOG%"
echo Logging top network consumers every 30s. Press Ctrl+C to stop.
:LOOP
echo. >> "%LOG%"
echo [%time%] >> "%LOG%"
powershell -NoProfile -Command ^
  "Get-NetTCPConnection | Group-Object OwningProcess | ^
   ForEach-Object { ^
     $proc=Get-Process -Id $_.Name -ErrorAction SilentlyContinue; ^
     [PSCustomObject]@{PID=$_.Name;Name=$proc.Name;Connections=$_.Count} ^
   } | Sort-Object Connections -Descending | Select-Object -First 10 | ^
   Format-Table -AutoSize | Out-File '%LOG%' -Append"
timeout /t 30 /nobreak >nul
goto LOOP
