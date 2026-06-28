@echo off
echo =========================
echo Backing up Documents Folder
echo =========================
set source="%USERPROFILE%\Documents"
set destination="C:\Backup\Documents_%date:~-4,4%%date:~-10,2%%date:~-7,2%"
echo Source: %source%
echo Destination: %destination%
echo.
xcopy %source% %destination% /E /I /C /Y
echo.
echo Backup Finished!
pause
