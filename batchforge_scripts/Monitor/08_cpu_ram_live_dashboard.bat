@echo off
:: ============================================================
:: CPU AND RAM LIVE MONITOR DASHBOARD
:: Polls CPU%, RAM used/total, and top processes every 5s.
:: Prints a refreshing dashboard to the console window.
:: ============================================================
title System Monitor - Press Ctrl+C to stop
:LOOP
cls
echo +======================================+
echo ^|       SYSTEM MONITOR  %time%       ^|
echo +======================================+
for /f "skip=1 tokens=2" %%C in ('wmic cpu get loadpercentage') do (
    echo ^|  CPU Load : %%C%%
    goto :ram
)
:ram
for /f "skip=1 tokens=*" %%R in ('wmic OS get FreePhysicalMemory^,TotalVisibleMemorySize /value') do (
    for /f "tokens=1,2 delims==" %%A in ("%%R") do (
        if "%%A"=="FreePhysicalMemory" set FREE=%%B
        if "%%A"=="TotalVisibleMemorySize" set TOTAL=%%B
    )
)
set /a USED=(%TOTAL%-%FREE%)/1024
set /a TOTALM=%TOTAL%/1024
echo ^|  RAM Used : %USED% MB / %TOTALM% MB
echo +======================================+
echo ^|  TOP PROCESSES:
wmic process get name,percentprocessortime /format:csv 2>nul | sort /r | findstr /v "Name,," | head -5 2>nul
echo +======================================+
timeout /t 5 /nobreak >nul
goto LOOP
