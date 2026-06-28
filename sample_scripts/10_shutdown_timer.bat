@echo off
echo =========================
echo Shutdown Timer
echo =========================
set /p minutes="Enter minutes until shutdown (e.g. 60): "
set /a seconds=%minutes%*60
shutdown -s -t %seconds%
echo.
echo System will shut down in %minutes% minutes.
echo To cancel this later, run 'shutdown -a' in the command prompt.
pause
