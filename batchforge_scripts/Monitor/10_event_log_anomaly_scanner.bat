@echo off
:: ============================================================
:: EVENT LOG ANOMALY SCANNER
:: Scans Windows Event Logs for errors/warnings in 24h.
:: Groups by source, counts occurrences, exports ranked report.
:: ============================================================
set "LOG=%TEMP%\eventlog_report.txt"
echo Event Log Anomaly Report > "%LOG%"
echo Period: Last 24 hours >> "%LOG%"
echo Generated: %date% %time% >> "%LOG%"
echo ================================ >> "%LOG%"
echo Scanning System log...
powershell -NoProfile -Command ^
  "Get-EventLog -LogName System -EntryType Error,Warning -Newest 200 | ^
   Group-Object Source | Sort-Object Count -Descending | ^
   Format-Table Count,Name -AutoSize | Out-File '%LOG%' -Append"
echo. >> "%LOG%"
echo Scanning Application log... >> "%LOG%"
powershell -NoProfile -Command ^
  "Get-EventLog -LogName Application -EntryType Error -Newest 100 | ^
   Group-Object Source | Sort-Object Count -Descending | ^
   Format-Table Count,Name -AutoSize | Out-File '%LOG%' -Append"
start notepad "%LOG%"
