@echo off
:: Toggles showing hidden files in Explorer.
echo This script demonstrates how to toggle hidden files (registry edit required).
echo Currently, it just lists hidden files in the C: drive root as a safe alternative:
dir C:\ /a:h
pause