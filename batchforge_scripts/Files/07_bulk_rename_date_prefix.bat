@echo off
:: ============================================================
:: RENAME FILES IN BULK WITH DATE PREFIX
:: Adds today's date as a prefix to every file in a folder.
:: Great for photo dumps and report archives.
:: ============================================================
setlocal enabledelayedexpansion
set "FOLDER=C:\Photos\Import"
set "PREFIX=%date:~10,4%%date:~4,2%%date:~7,2%"
cd /d "%FOLDER%"
for %%F in (*.*) do (
    if not "%%~nxF"=="%~nx0" (
        ren "%%F" "%PREFIX%_%%F"
        echo Renamed: %%F to %PREFIX%_%%F
    )
)
echo All files renamed. Done.
