@echo off
:: ============================================================
:: DEAD CODE FILE DETECTOR
:: Scans project for .py/.js/.ts files not modified in 90+
:: days. These are candidates for dead/unused code review.
:: ============================================================
set "ROOT=C:\Projects\MyApp"
set "OUT=%TEMP%\dead_code.txt"
echo Dead Code Candidates (not modified in 90+ days) > "%OUT%"
echo Project: %ROOT% >> "%OUT%"
echo ============================================== >> "%OUT%"
forfiles /p "%ROOT%" /s /m *.py /d -90 /c "cmd /c echo @path >> \"%OUT%\"" 2>nul
forfiles /p "%ROOT%" /s /m *.js /d -90 /c "cmd /c echo @path >> \"%OUT%\"" 2>nul
forfiles /p "%ROOT%" /s /m *.ts /d -90 /c "cmd /c echo @path >> \"%OUT%\"" 2>nul
echo.
type "%OUT%"
echo Full list: %OUT%
pause
