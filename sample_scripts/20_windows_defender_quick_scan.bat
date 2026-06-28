@echo off
:: Runs a quick Windows Defender scan using MpCmdRun.exe
echo Initiating Windows Defender Quick Scan...
"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -Scan -ScanType 1
echo Scan complete.
pause