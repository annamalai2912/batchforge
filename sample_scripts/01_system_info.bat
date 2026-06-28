@echo off
echo =========================
echo SYSTEM INFORMATION
echo =========================
systeminfo | findstr /c:"OS Name"
systeminfo | findstr /c:"OS Version"
systeminfo | findstr /c:"System Type"
systeminfo | findstr /c:"Total Physical Memory"
echo =========================
pause
