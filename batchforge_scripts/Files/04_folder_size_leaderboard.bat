@echo off
setlocal enabledelayedexpansion
:: ============================================================
:: FOLDER SIZE ANALYSER WITH LEADERBOARD
:: Scans every subfolder, calculates size in MB,
:: and prints a ranked list from largest to smallest.
:: ============================================================
set "ROOT=C:\Users\%USERNAME%"
set "LOG=%TEMP%\folder_sizes.txt"
echo Folder Size Report - %date% > "%LOG%"
echo ============================== >> "%LOG%"
echo Scanning... (may take a moment)
for /d %%D in ("%ROOT%\*") do (
    set "SIZE=0"
    for /r "%%D" %%F in (*) do set /a SIZE+=%%~zF 2>nul
    set /a SIZEMB=!SIZE! / 1048576
    echo !SIZEMB! MB  %%~nxD >> "%LOG%"
)
sort /r "%LOG%" > "%TEMP%\sorted_folders.txt"
type "%TEMP%\sorted_folders.txt"
echo.
echo Full report: %LOG%
pause
