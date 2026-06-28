@echo off
setlocal enabledelayedexpansion
:: ============================================================
:: SMART FOLDER WATCHER WITH AUTO-SORT
:: Watches a folder every 60 seconds and auto-sorts new files
:: by extension into subfolders.
:: ============================================================
set "WATCH=C:\Users\%USERNAME%\Downloads"
echo Watching %WATCH% -- press Ctrl+C to stop
:LOOP
for %%F in ("%WATCH%\*.*") do (
    if not "%%~xF"=="" (
        set "EXT=%%~xF"
        set "EXT=!EXT:~1!"
        set "DEST=%WATCH%\Sorted\!EXT!"
        if not exist "!DEST!" mkdir "!DEST!"
        move "%%F" "!DEST!\\" >nul 2>&1
        echo [%time%] Moved %%~nxF to !EXT!
    )
)
timeout /t 60 /nobreak >nul
goto LOOP
