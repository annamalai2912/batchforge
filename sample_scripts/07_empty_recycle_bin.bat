@echo off
echo =========================
echo Emptying Recycle Bin
echo =========================
rd /s /q %systemdrive%\$Recycle.bin
echo Recycle Bin Emptied!
pause
