@echo off
:: ============================================================
:: NETWORK ADAPTER RESET WIZARD
:: Detects all adapters, disables then re-enables each one.
:: Resets TCP/IP stack and routing table.
:: Run as Administrator.
:: ============================================================
echo Network Adapter Reset Wizard
echo =============================
echo [1/4] Resetting TCP/IP stack...
netsh int ip reset >nul
echo [2/4] Resetting Winsock...
netsh winsock reset >nul
echo [3/4] Flushing DNS...
ipconfig /flushdns >nul
echo [4/4] Cycling all adapters...
powershell -NoProfile -Command ^
  "Get-NetAdapter | ForEach-Object { ^
    Write-Host 'Cycling:' $_.Name; ^
    Disable-NetAdapter -Name $_.Name -Confirm:$false; ^
    Start-Sleep -Seconds 2; ^
    Enable-NetAdapter -Name $_.Name -Confirm:$false ^
  }"
echo.
echo All adapters reset at %time%
ipconfig /all
pause
