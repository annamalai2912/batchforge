@echo off
:: ============================================================
:: LOGIN ATTEMPT BRUTE-FORCE DETECTOR
:: Mines Security event log for Event ID 4625 (failed logins).
:: Groups by username, flags accounts with 5+ failures.
:: Run as Administrator.
:: ============================================================
echo Scanning for failed login attempts (Event 4625)...
set "OUT=%TEMP%\bruteforce_report.txt"
echo Brute-Force Detection Report > "%OUT%"
echo Date: %date% %time% >> "%OUT%"
echo ============================== >> "%OUT%"
powershell -NoProfile -Command ^
  "Get-WinEvent -FilterHashtable @{LogName='Security';Id=4625} -MaxEvents 500 -ErrorAction SilentlyContinue | ^
   Select-Object TimeCreated, ^
     @{N='User';E={$_.Properties[5].Value}}, ^
     @{N='IP';E={$_.Properties[19].Value}} | ^
   Group-Object User | Sort-Object Count -Descending | ^
   Where-Object Count -ge 5 | ^
   Format-Table Count,Name -AutoSize | Out-File '%OUT%' -Append"
start notepad "%OUT%"
