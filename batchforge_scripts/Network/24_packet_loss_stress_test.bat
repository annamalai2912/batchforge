@echo off
:: ============================================================
:: NETWORK PACKET LOSS STRESS TESTER
:: Pings 5 major DNS servers simultaneously.
:: Reports latency min/max/avg and packet loss %.
:: ============================================================
echo Network Connectivity Health Check
echo ==================================
set HOSTS=8.8.8.8 1.1.1.1 9.9.9.9 208.67.222.222 4.2.2.2
for %%H in (%HOSTS%) do (
    echo.
    echo Testing %%H...
    ping -n 10 %%H | findstr "packets Average Minimum Maximum"
)
echo.
echo Done at %time%
pause
