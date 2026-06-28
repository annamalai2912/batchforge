@echo off
:: ============================================================
:: POWER PLAN SWITCHER WITH PROFILE PRESETS
:: Switches between Performance, Balanced, or Silent modes.
:: Call with argument: 39_power_plan_switcher.bat performance
:: ============================================================
set "MODE=%1"
if "%MODE%"=="" (
    set /p MODE="Enter mode [performance/balanced/silent]: "
)
if /i "%MODE%"=="performance" (
    powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
    powercfg /change standby-timeout-ac 0
    powercfg /change monitor-timeout-ac 15
    echo Performance mode: sleep OFF, screen 15min
) else if /i "%MODE%"=="balanced" (
    powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e
    powercfg /change standby-timeout-ac 30
    powercfg /change monitor-timeout-ac 10
    echo Balanced mode: sleep 30min, screen 10min
) else if /i "%MODE%"=="silent" (
    powercfg /setactive a1841308-3541-4fab-bc81-f71556f20b4a
    powercfg /change standby-timeout-ac 10
    powercfg /change monitor-timeout-ac 3
    echo Silent mode: sleep 10min, screen 3min
) else (
    echo Unknown mode. Use: performance, balanced, or silent
)
pause
