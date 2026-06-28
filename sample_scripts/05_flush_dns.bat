@echo off
echo =========================
echo Flushing DNS Cache
echo =========================
ipconfig /flushdns
echo.
echo =========================
echo Renewing IP Address
echo =========================
ipconfig /renew
echo.
echo Done!
pause
