@echo off
:: Shows how to schedule a daily task using schtasks.
echo To schedule a daily backup, run this as Admin:
echo schtasks /create /tn "DailyBackup" /tr "C:\backup.bat" /sc daily /st 12:00
pause