@echo off
:: ============================================================
:: SCHEDULED TASK AUDIT REPORT
:: Lists all scheduled tasks with status, last/next run time,
:: and exit code. Exports to CSV.
:: ============================================================
set "OUT=%USERPROFILE%\Desktop\task_audit_%date:~10,4%%date:~4,2%%date:~7,2%.csv"
echo Exporting scheduled task audit...
powershell -NoProfile -Command ^
  "Get-ScheduledTask | ForEach-Object { ^
    $info = Get-ScheduledTaskInfo $_.TaskName -ErrorAction SilentlyContinue; ^
    [PSCustomObject]@{ ^
        Name=$_.TaskName; State=$_.State; ^
        LastRun=$info.LastRunTime; NextRun=$info.NextRunTime; ^
        LastResult=$info.LastTaskResult ^
    } ^
  } | Export-Csv -Path '%OUT%' -NoTypeInformation"
echo Saved: %OUT%
start excel "%OUT%" 2>nul || start notepad "%OUT%"
