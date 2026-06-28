@echo off
:: ============================================================
:: BITLOCKER STATUS AUDIT - ALL DRIVES
:: Checks every volume for BitLocker encryption status,
:: protection status, and flags unencrypted fixed drives.
:: ============================================================
echo BitLocker Audit Report
echo ======================
powershell -NoProfile -Command ^
  "Get-BitLockerVolume | Select-Object MountPoint,VolumeStatus,ProtectionStatus,EncryptionPercentage,LockStatus | ^
   Format-Table -AutoSize"
echo.
powershell -NoProfile -Command ^
  "$vols=Get-BitLockerVolume; foreach($v in $vols){ ^
   if($v.ProtectionStatus -eq 'Off' -and $v.VolumeType -eq 'OperatingSystem'){ ^
     Write-Warning ('UNENCRYPTED OS DRIVE: ' + $v.MountPoint) ^
   }}"
pause
