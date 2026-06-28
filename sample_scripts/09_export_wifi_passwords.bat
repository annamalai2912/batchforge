@echo off
echo =========================
echo Export Wi-Fi Passwords
echo =========================
set export_folder="%USERPROFILE%\Desktop\WiFi_Profiles"
md %export_folder% 2>nul
netsh wlan export profile key=clear folder=%export_folder%
echo.
echo Wi-Fi Profiles exported to your Desktop in the WiFi_Profiles folder.
echo (Warning: These files contain cleartext passwords).
pause
