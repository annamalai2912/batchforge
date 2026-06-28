@echo off
:: ============================================================
:: GIT REPO BULK PULLER
:: Scans a parent folder for all Git repos and runs
:: git pull on each one automatically.
:: ============================================================
set "REPOS_DIR=C:\Projects"
echo Pulling all Git repos in %REPOS_DIR%...
echo =========================================
for /d %%D in ("%REPOS_DIR%\*") do (
    if exist "%%D\.git" (
        echo.
        echo [%%~nD]
        cd /d "%%D"
        git pull
    )
)
echo.
echo All repos updated at %date% %time%
pause
