@echo off
:: Renames all .txt files in the current directory to include a prefix.
:: Safe and non-destructive.
echo Renaming text files...
for %%f in (*.txt) do (
    if not exist "prefix_%%f" ren "%%f" "prefix_%%f"
)
echo Done.
pause