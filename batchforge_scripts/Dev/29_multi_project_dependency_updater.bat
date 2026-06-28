@echo off
:: ============================================================
:: MULTI-PROJECT DEPENDENCY UPDATER
:: Scans all subdirs for package.json (Node) or
:: requirements.txt (Python) and updates dependencies in each.
:: ============================================================
set "ROOT=C:\Projects"
echo Updating dependencies in all projects under %ROOT%...
for /d %%D in ("%ROOT%\*") do (
    echo.
    echo === %%~nD ===
    if exist "%%D\package.json" (
        cd /d "%%D"
        echo [Node] Running npm update...
        npm update 2>&1
    )
    if exist "%%D\requirements.txt" (
        cd /d "%%D"
        echo [Python] Updating pip packages...
        pip install -r requirements.txt --upgrade -q 2>&1
    )
)
echo.
echo All projects updated at %date% %time%
pause
