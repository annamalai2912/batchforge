@echo off
:: ============================================================
:: ENVIRONMENT VARIABLE FULL SNAPSHOT
:: Captures all system and user environment variables sorted
:: alphabetically. Use before/after for comparison.
:: ============================================================
set "OUT=%USERPROFILE%\Desktop\env_snapshot_%date:~10,4%%date:~4,2%%date:~7,2%.txt"
echo Environment Variable Snapshot > "%OUT%"
echo Machine: %COMPUTERNAME% >> "%OUT%"
echo Date: %date% %time% >> "%OUT%"
echo ================================ >> "%OUT%"
echo. >> "%OUT%"
echo --- SYSTEM VARIABLES --- >> "%OUT%"
powershell -NoProfile -Command ^
  "[System.Environment]::GetEnvironmentVariables('Machine').GetEnumerator() | Sort-Object Key | ^
   ForEach-Object { '{0}={1}' -f $_.Key,$_.Value } | Out-File '%OUT%' -Append"
echo. >> "%OUT%"
echo --- USER VARIABLES --- >> "%OUT%"
powershell -NoProfile -Command ^
  "[System.Environment]::GetEnvironmentVariables('User').GetEnumerator() | Sort-Object Key | ^
   ForEach-Object { '{0}={1}' -f $_.Key,$_.Value } | Out-File '%OUT%' -Append"
echo Saved: %OUT%
start notepad "%OUT%"
