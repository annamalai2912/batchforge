@echo off
:: ============================================================
:: AUTO-SCREENSHOT ON SCHEDULE
:: Takes a full-screen screenshot every N minutes.
:: Useful for activity logging or kiosk monitoring.
:: ============================================================
set "OUTDIR=C:\Screenshots"
set "INTERVAL=5"
if not exist "%OUTDIR%" mkdir "%OUTDIR%"
echo Taking screenshots every %INTERVAL% minutes. Press Ctrl+C to stop.
:LOOP
set "TS=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%"
set "TS=%TS: =0%"
powershell -NoProfile -WindowStyle Hidden -Command ^
  "Add-Type -AssemblyName System.Windows.Forms,System.Drawing; ^
   $s=[System.Windows.Forms.Screen]::PrimaryScreen.Bounds; ^
   $bmp=New-Object System.Drawing.Bitmap($s.Width,$s.Height); ^
   $g=[System.Drawing.Graphics]::FromImage($bmp); ^
   $g.CopyFromScreen($s.Location,[System.Drawing.Point]::Empty,$s.Size); ^
   $bmp.Save('%OUTDIR%\ss_%TS%.png'); $g.Dispose(); $bmp.Dispose()"
echo Saved ss_%TS%.png
timeout /t %INTERVAL%0 /nobreak >nul
goto LOOP
