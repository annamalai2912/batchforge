@echo off
:: ============================================================
:: HYPER-V SNAPSHOT AUTOMATOR
:: Takes a checkpoint of every running Hyper-V VM with a
:: timestamped name. Removes checkpoints older than 7 days.
:: Run as Administrator on Hyper-V host.
:: ============================================================
echo Hyper-V Snapshot Automator
echo ===========================
set "TS=%date:~10,4%-%date:~4,2%-%date:~7,2%"
echo Creating snapshots for all running VMs...
powershell -NoProfile -Command ^
  "Get-VM | Where-Object State -eq Running | ForEach-Object { ^
    $name=$_.Name; $snap='AutoSnap-%TS%'; ^
    Checkpoint-VM -Name $name -SnapshotName $snap; ^
    Write-Host 'Snapshot created:' $name '->' $snap ^
  }"
echo.
echo Removing snapshots older than 7 days...
powershell -NoProfile -Command ^
  "Get-VM | ForEach-Object { ^
    Get-VMSnapshot -VMName $_.Name | ^
    Where-Object {$_.CreationTime -lt (Get-Date).AddDays(-7)} | ^
    ForEach-Object { Remove-VMSnapshot $_; Write-Host 'Removed:' $_.Name } ^
  }"
echo.
echo Done at %time%
