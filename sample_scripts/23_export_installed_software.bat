@echo off
:: Exports a list of installed software to a text file using WMIC.
echo Exporting installed software list to software_list.txt...
wmic product get name,version > software_list.txt
echo Done.
pause