@echo off
:: ============================================================
:: RAM CACHE FLUSH + DNS + WINSOCK + IP RENEWAL COMBO
:: The ultimate network and memory refresh in one script.
:: Run as Administrator for full effect.
:: ============================================================
echo === System Refresh Starting ===
echo.
echo [1/4] Flushing DNS cache...
ipconfig /flushdns
echo.
echo [2/4] Resetting Winsock...
netsh winsock reset >nul
echo.
echo [3/4] Releasing and renewing IP...
ipconfig /release >nul
ipconfig /renew >nul
echo.
echo [4/4] Clearing standby RAM list...
powershell -NoProfile -Command ^
  "& { Add-Type -TypeDefinition 'using System;using System.Runtime.InteropServices;public class Mem{[DllImport(\"psapi.dll\")]public static extern bool EmptyWorkingSet(IntPtr h);}'; ^
   Get-Process | ForEach-Object { [Mem]::EmptyWorkingSet($_.Handle) } }" 2>nul
echo.
echo === Refresh complete at %time% ===
pause
