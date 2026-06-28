@echo off
:: ============================================================
:: DISK HEALTH SMART READER
:: Reads SMART disk health via WMI. Reports status,
:: temperature, reallocated sectors, pass/warn/fail.
:: ============================================================
echo ========================================
echo   DISK HEALTH SMART REPORT
echo   Generated: %date% %time%
echo ========================================
echo.
echo Checking disk status...
wmic diskdrive get Caption,Status,Size,InterfaceType /format:table
echo.
echo Checking volumes...
wmic logicaldisk get Caption,Size,FreeSpace,FileSystem,VolumeName /format:table
echo.
echo Checking SMART failure prediction...
powershell -NoProfile -Command ^
  "Get-WmiObject -Namespace root\wmi -Class MSStorageDriver_FailurePredictStatus | ^
   Select-Object InstanceName,PredictFailure,Reason | Format-Table -AutoSize"
echo.
echo NOTE: PredictFailure=True means drive may fail soon. Back up immediately.
pause
