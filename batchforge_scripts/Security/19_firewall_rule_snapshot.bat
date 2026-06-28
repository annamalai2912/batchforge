@echo off
:: ============================================================
:: FIREWALL RULE SNAPSHOT AND DIFF
:: Exports all firewall rules to a timestamped CSV.
:: Run before and after software installs to see what changed.
:: ============================================================
set "TS=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%"
set "TS=%TS: =0%"
set "OUT=%USERPROFILE%\Desktop\fw_rules_%TS%.csv"
echo Exporting firewall rules...
powershell -NoProfile -Command ^
  "Get-NetFirewallRule | Select-Object Name,DisplayName,Direction,Action,Enabled,Profile | ^
   Export-Csv -Path '%OUT%' -NoTypeInformation"
echo Saved: %OUT%
echo Compare two snapshots with: fc snapshot1.csv snapshot2.csv
start notepad "%OUT%"
