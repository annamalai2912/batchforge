@echo off
:: ============================================================
:: WINDOWS SERVICE HEALTH WATCHDOG
:: Checks critical services. If stopped, auto-restarts them
:: and logs every action with timestamp to a watchdog log.
:: Schedule this to run every 5 minutes via Task Scheduler.
:: ============================================================
set "LOG=C:\Logs\watchdog.log"
if not exist "C:\Logs" mkdir "C:\Logs"
set SERVICES=wuauserv Spooler AudioSrv Dhcp
for %%S in (%SERVICES%) do (
    sc query "%%S" | findstr "RUNNING" >nul
    if errorlevel 1 (
        echo [%date% %time%] %%S was STOPPED. Restarting... >> "%LOG%"
        net start "%%S" >nul 2>&1
        if errorlevel 1 (
            echo [%date% %time%] FAILED to restart %%S >> "%LOG%"
        ) else (
            echo [%date% %time%] %%S restarted OK >> "%LOG%"
        )
    ) else (
        echo [%date% %time%] %%S OK >> "%LOG%"
    )
)
echo Watchdog check complete. Log: %LOG%
