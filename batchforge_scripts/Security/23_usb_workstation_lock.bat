@echo off
:: ============================================================
:: LOCK WORKSTATION ON USB REMOVE
:: Polls for a specific USB drive letter. When removed,
:: instantly locks the workstation. Acts as a physical key.
:: ============================================================
set "USB=E:"
echo Watching for USB key on %USB%...
echo Remove the drive to lock the workstation.
:WATCH
timeout /t 3 /nobreak >nul
if not exist "%USB%\\" (
    echo USB removed at %time%. Locking...
    rundll32.exe user32.dll,LockWorkStation
    goto :END
)
goto WATCH
:END
echo Workstation locked.
