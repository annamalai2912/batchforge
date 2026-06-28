@echo off
:: ============================================================
:: AUTO GIT COMMIT AND PUSH ON CHANGE
:: Watches a Git repo every 60s. If uncommitted changes exist,
:: auto-stages, commits with timestamp, and pushes to origin.
:: ============================================================
set "REPO=C:\Projects\MyApp"
cd /d "%REPO%"
echo Watching %REPO% for changes. Press Ctrl+C to stop.
:LOOP
git status --porcelain > "%TEMP%\gitstatus.tmp"
for %%A in ("%TEMP%\gitstatus.tmp") do if %%~zA GTR 0 (
    echo [%time%] Changes detected. Committing...
    git add -A
    git commit -m "Auto-commit: %date% %time%"
    git push origin HEAD
    echo [%time%] Pushed to origin.
)
timeout /t 60 /nobreak >nul
goto LOOP
