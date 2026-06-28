@echo off
:: Prompts for minutes until shutdown and schedules it.
set /p Mins="Enter minutes until shutdown (0 to cancel): "
if "%Mins%"=="0" (
    shutdown -a
    echo Shutdown cancelled.
) else (
    set /a Secs=%Mins%*60
    shutdown -s -t %Secs%
    echo System will shut down in %Mins% minutes.
)
pause