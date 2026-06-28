@echo off
:: Generates a Windows battery report (for laptops).
echo Generating battery report...
powercfg /batteryreport /output "battery_report.html"
echo Report saved to battery_report.html
pause