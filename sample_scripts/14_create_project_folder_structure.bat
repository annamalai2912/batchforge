@echo off
:: Creates a standard project directory structure.
set /p ProjectName="Enter Project Name: "
mkdir "%ProjectName%"
cd "%ProjectName%"
mkdir src
mkdir docs
mkdir tests
mkdir assets
echo Project %ProjectName% created successfully.
pause