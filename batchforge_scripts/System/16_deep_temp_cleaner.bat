@echo off
:: ============================================================
:: TEMP FILE DEEP CLEANER
:: Wipes %TEMP%, Windows Temp, Prefetch, browser caches,
:: and thumbnail cache. Run as Administrator.
:: ============================================================
echo Deep Temp Cleaner
echo =================
for %%D in (
    "%TEMP%"
    "C:\Windows\Temp"
    "C:\Windows\Prefetch"
    "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache"
    "%LOCALAPPDATA%\Microsoft\Windows\Explorer"
) do (
    if exist "%%~D" (
        echo Cleaning %%~D ...
        del /f /s /q "%%~D\*" >nul 2>&1
    )
)
echo.
echo Cleaning thumbnail cache...
taskkill /f /im explorer.exe >nul 2>&1
del /f /s /q "%LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_*.db" >nul 2>&1
start explorer.exe
echo.
echo Deep clean complete at %time%
pause
