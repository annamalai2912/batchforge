@echo off
:: Example script to organize files by extension into folders.
echo Organizing files into Images, Documents, and Media folders...
if not exist "Images" mkdir Images
if not exist "Documents" mkdir Documents
if not exist "Media" mkdir Media
echo Move commands would go here (disabled for safety).
pause