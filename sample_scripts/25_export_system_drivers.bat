@echo off
:: Exports a list of installed drivers.
echo Exporting driver list to drivers.txt...
driverquery > drivers.txt
echo Done.
pause