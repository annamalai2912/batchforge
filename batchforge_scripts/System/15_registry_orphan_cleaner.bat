@echo off
:: ============================================================
:: REGISTRY CLEANER FOR BROKEN APP ENTRIES
:: Scans Uninstall registry keys for entries pointing to
:: non-existent install paths. Lists orphaned entries.
:: ============================================================
echo Scanning for broken registry uninstall entries...
echo =================================================
powershell -NoProfile -Command ^
  "$reg='HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall'; ^
   Get-ChildItem $reg | ForEach-Object { ^
     $loc=(Get-ItemProperty $_.PSPath -ErrorAction SilentlyContinue).InstallLocation; ^
     if($loc -and $loc.Length -gt 0 -and !(Test-Path $loc)){ ^
       Write-Host 'ORPHAN:' (Get-ItemProperty $_.PSPath).DisplayName ' -> ' $loc ^
     } ^
   }"
echo.
echo Review above. Remove orphans via: regedit > HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall
pause
