import os

scripts = {
    "01_auto_backup_documents.bat": """@echo off
:: ==========================================
:: Auto Backup Documents
:: Copies all files from Documents to a Backup folder on C:
:: ==========================================
echo Starting backup...
xcopy "%USERPROFILE%\\Documents\\*.*" "C:\\Backup_Documents\\" /s /e /y /i
echo Backup complete!
pause""",

    "02_clean_temp_files.bat": """@echo off
:: ==========================================
:: Clean Temp Files
:: Safely deletes temporary files to free up space.
:: ==========================================
echo Cleaning Temp folder...
del /q /f /s "%TEMP%\\*.*"
echo Cleanup finished.
pause""",

    "03_sync_directories.bat": """@echo off
:: ==========================================
:: Sync Directories (Mirror)
:: Uses Robocopy to mirror Source to Destination.
:: Edit paths before use.
:: ==========================================
set "SRC=C:\\SourceFolder"
set "DST=D:\\DestinationFolder"
echo Syncing %SRC% to %DST%...
robocopy "%SRC%" "%DST%" /MIR /Z /W:5
pause""",

    "04_start_dev_environment.bat": """@echo off
:: ==========================================
:: Start Dev Environment
:: Launches common development tools simultaneously.
:: ==========================================
echo Starting IDE and Browser...
start code .
start msedge https://github.com
start cmd
echo Environment ready.
pause""",

    "05_shutdown_end_of_day.bat": """@echo off
:: ==========================================
:: End of Day Shutdown
:: Schedules a shutdown in 60 minutes.
:: ==========================================
echo Scheduling PC shutdown in 60 minutes...
shutdown -s -t 3600
echo Run 'shutdown -a' to cancel.
pause""",

    "06_empty_recycle_bin.bat": """@echo off
:: ==========================================
:: Empty Recycle Bin
:: Uses PowerShell to empty the recycle bin silently.
:: ==========================================
echo Emptying Recycle Bin...
powershell -NoProfile -Command "Clear-RecycleBin -Force"
echo Done.
pause""",

    "07_restart_networking.bat": """@echo off
:: ==========================================
:: Restart Networking
:: Releases and renews IP address, flushes DNS.
:: ==========================================
echo Releasing IP...
ipconfig /release
echo Renewing IP...
ipconfig /renew
echo Flushing DNS...
ipconfig /flushdns
echo Network reset complete.
pause""",

    "08_bulk_rename_prefix.bat": """@echo off
:: ==========================================
:: Bulk Rename (Prefix)
:: Adds a prefix to all .txt files in the current folder.
:: ==========================================
set "PREFIX=Processed_"
echo Adding prefix %PREFIX% to text files...
for %%f in (*.txt) do (
    ren "%%f" "%PREFIX%%%f"
)
echo Done.
pause""",

    "09_organize_downloads.bat": """@echo off
:: ==========================================
:: Organize Downloads
:: Moves files into categorized folders based on extension.
:: ==========================================
cd /d "%USERPROFILE%\\Downloads"
if not exist "Images" mkdir Images
if not exist "Documents" mkdir Documents
if not exist "Installers" mkdir Installers

move *.jpg Images\\ >nul 2>&1
move *.png Images\\ >nul 2>&1
move *.pdf Documents\\ >nul 2>&1
move *.docx Documents\\ >nul 2>&1
move *.exe Installers\\ >nul 2>&1
echo Downloads organized!
pause""",

    "10_auto_git_commit.bat": """@echo off
:: ==========================================
:: Auto Git Commit
:: Stages all changes and commits with a timestamp.
:: ==========================================
echo Staging changes...
git add .
echo Committing...
git commit -m "Auto-commit: %date% %time%"
echo Pushing...
git push
pause""",

    "11_ping_server_monitor.bat": """@echo off
:: ==========================================
:: Server Ping Monitor
:: Pings a server and logs the output.
:: ==========================================
set "SERVER=8.8.8.8"
echo Pinging %SERVER% and logging to ping_log.txt...
ping %SERVER% -n 5 >> ping_log.txt
echo Done.
pause""",

    "12_clear_browser_cache.bat": """@echo off
:: ==========================================
:: Clear Browser Cache (Basic)
:: Kills Chrome/Edge and clears local temp cache data.
:: ==========================================
taskkill /F /IM msedge.exe >nul 2>&1
taskkill /F /IM chrome.exe >nul 2>&1
echo Browsers closed. Cache clearing would happen here (needs precise paths).
pause""",

    "13_auto_extract_zips.bat": """@echo off
:: ==========================================
:: Auto Extract ZIPs
:: Extracts all zip files in the current folder using PowerShell.
:: ==========================================
echo Extracting ZIP files...
powershell -NoProfile -Command "Get-ChildItem '*.zip' | ForEach-Object { Expand-Archive $_.FullName -DestinationPath $_.BaseName -Force }"
echo Extraction complete.
pause""",

    "14_schedule_system_scan.bat": """@echo off
:: ==========================================
:: Schedule System Scan
:: Creates a scheduled task to run Defender scan weekly.
:: Requires Administrator.
:: ==========================================
echo Creating scheduled task for Windows Defender...
schtasks /create /tn "WeeklyDefenderScan" /tr "\"%ProgramFiles%\\Windows Defender\\MpCmdRun.exe\" -Scan -ScanType 1" /sc weekly /d SUN /st 02:00
pause""",

    "15_start_local_server.bat": """@echo off
:: ==========================================
:: Start Local HTTP Server
:: Starts a Python HTTP server on port 8000.
:: ==========================================
echo Starting Python HTTP server...
python -m http.server 8000
pause""",

    "16_close_distracting_apps.bat": """@echo off
:: ==========================================
:: Focus Mode (Close Distractions)
:: Force closes common distracting applications.
:: ==========================================
echo Closing distractions...
taskkill /F /IM discord.exe >nul 2>&1
taskkill /F /IM spotify.exe >nul 2>&1
taskkill /F /IM steam.exe >nul 2>&1
echo Focus mode activated!
pause""",

    "17_daily_log_creator.bat": """@echo off
:: ==========================================
:: Daily Log Creator
:: Creates a new text file named with today's date.
:: ==========================================
set "TODAY=%date:~-4,4%_%date:~-10,2%_%date:~-7,2%"
set "FILENAME=Log_%TODAY%.txt"
echo Creating %FILENAME%...
echo === Daily Log: %TODAY% === > "%FILENAME%"
start notepad "%FILENAME%"
pause"""
}

target_dir = r"e:\Batch Scrippting\batchforge_scripts\Automation"
os.makedirs(target_dir, exist_ok=True)

for name, content in scripts.items():
    with open(os.path.join(target_dir, name), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully generated 17 automation scripts in {target_dir}")
