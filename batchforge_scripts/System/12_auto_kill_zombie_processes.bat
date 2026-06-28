@echo off
:: ============================================================
:: AUTO-KILL ZOMBIE PROCESSES
:: Detects processes running 2h+ with no window and no CPU.
:: Prompts to terminate them as suspected zombies.
:: ============================================================
echo Scanning for zombie processes (2h+ runtime, 0 CPU)...
echo =====================================================
powershell -NoProfile -Command ^
  "Get-Process | Where-Object { ^
    $_.CPU -lt 0.1 -and ^
    $_.MainWindowTitle -eq '' -and ^
    ((Get-Date) - $_.StartTime).TotalHours -gt 2 ^
  } | Select-Object Id,Name,CPU,@{N='Hours';E={[math]::Round(((Get-Date)-$_.StartTime).TotalHours,1)}} | ^
  Format-Table -AutoSize"
echo.
set /p KILLPID="Enter PID to kill (Enter to skip): "
if not "%KILLPID%"=="" (
    taskkill /PID %KILLPID% /F
    echo Process %KILLPID% terminated.
)
pause
