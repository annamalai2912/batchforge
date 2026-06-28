@echo off
:: ============================================================
:: MULTI-MACHINE REMOTE COMMAND SENDER
:: Reads machine hostnames from a text file and runs the same
:: command on each via WinRM (PowerShell Invoke-Command).
:: Requires WinRM enabled on target machines.
:: ============================================================
set "MACHINES=C:\Scripts\machines.txt"
set "CMD=ipconfig /all"
echo Remote Command Executor
echo Command: %CMD%
echo Targets: %MACHINES%
echo =======================
for /f "tokens=*" %%M in (%MACHINES%) do (
    echo.
    echo --- %%M ---
    powershell -NoProfile -Command ^
      "Invoke-Command -ComputerName '%%M' -ScriptBlock { %CMD% } -ErrorAction SilentlyContinue" ^
      2>nul || echo [FAILED] Could not reach %%M
)
echo.
echo Done at %time%
pause
