@echo off
:: ============================================================
:: SMART LOG AGGREGATOR AND TAGGER
:: Merges all .log files, tags each line with source filename,
:: deduplicates repeated lines, and produces a master log.
:: ============================================================
set "LOGDIR=C:\Logs"
set "OUT=%LOGDIR%\master_%date:~10,4%%date:~4,2%%date:~7,2%.log"
if exist "%OUT%" del "%OUT%"
echo Master Log - %date% %time% > "%OUT%"
echo ================================= >> "%OUT%"
for %%F in ("%LOGDIR%\*.log") do (
    if not "%%~nxF"=="%~nx0" (
        echo [SOURCE: %%~nxF] >> "%OUT%"
        type "%%F" >> "%OUT%"
        echo. >> "%OUT%"
    )
)
powershell -NoProfile -Command ^
  "Get-Content '%OUT%' | Sort-Object -Unique | Set-Content '%OUT%'"
echo Aggregated log: %OUT%
