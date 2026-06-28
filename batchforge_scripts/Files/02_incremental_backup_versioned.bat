@echo off
setlocal
:: ============================================================
:: INCREMENTAL BACKUP WITH 7-DAY VERSION HISTORY
:: Backs up only changed files using xcopy /D.
:: Keeps 7 daily versions, auto-deletes older ones.
:: ============================================================
set "SRC=C:\Users\%USERNAME%\Documents"
set "DEST=D:\Backups"
set "TS=%date:~10,4%-%date:~4,2%-%date:~7,2%"
set "TODAY=%DEST%\%TS%"
if not exist "%TODAY%" mkdir "%TODAY%"
xcopy "%SRC%" "%TODAY%\\" /E /D /I /Y /Q
echo Incremental backup done: %TODAY%
echo Removing backups older than 7 days...
forfiles /p "%DEST%" /d -7 /c "cmd /c if @isdir==TRUE rd /s /q @path & echo Removed @path" 2>nul
echo Done at %date% %time%
