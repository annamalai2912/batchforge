import os

scripts = {
    # Productivity & Automation
    "11_bulk_file_renamer.bat": """@echo off
:: Renames all .txt files in the current directory to include a prefix.
:: Safe and non-destructive.
echo Renaming text files...
for %%f in (*.txt) do (
    if not exist "prefix_%%f" ren "%%f" "prefix_%%f"
)
echo Done.
pause""",
    
    "12_organize_downloads.bat": """@echo off
:: Example script to organize files by extension into folders.
echo Organizing files into Images, Documents, and Media folders...
if not exist "Images" mkdir Images
if not exist "Documents" mkdir Documents
if not exist "Media" mkdir Media
echo Move commands would go here (disabled for safety).
pause""",

    "13_daily_workspace_setup.bat": """@echo off
:: Opens common apps for a daily workspace.
echo Setting up daily workspace...
start notepad.exe
start calc.exe
:: Add your own apps here
echo Workspace ready.
pause""",

    "14_create_project_folder_structure.bat": """@echo off
:: Creates a standard project directory structure.
set /p ProjectName="Enter Project Name: "
mkdir "%ProjectName%"
cd "%ProjectName%"
mkdir src
mkdir docs
mkdir tests
mkdir assets
echo Project %ProjectName% created successfully.
pause""",

    "15_auto_shutdown_scheduler.bat": """@echo off
:: Prompts for minutes until shutdown and schedules it.
set /p Mins="Enter minutes until shutdown (0 to cancel): "
if "%Mins%"=="0" (
    shutdown -a
    echo Shutdown cancelled.
) else (
    set /a Secs=%Mins%*60
    shutdown -s -t %Secs%
    echo System will shut down in %Mins% minutes.
)
pause""",

    "16_schedule_daily_backup.bat": """@echo off
:: Shows how to schedule a daily task using schtasks.
echo To schedule a daily backup, run this as Admin:
echo schtasks /create /tn "DailyBackup" /tr "C:\\backup.bat" /sc daily /st 12:00
pause""",

    "17_app_launcher_group.bat": """@echo off
:: Launches a group of related applications.
echo Launching dev tools...
start cmd.exe
start explorer.exe
pause""",

    # Ethical Cyber & Security
    "18_check_open_ports.bat": """@echo off
:: Lists all listening ports on the system.
echo Checking open ports...
netstat -an | find "LISTEN"
pause""",

    "19_list_active_connections.bat": """@echo off
:: Lists established network connections.
echo Listing active connections...
netstat -an | find "ESTABLISHED"
pause""",

    "20_windows_defender_quick_scan.bat": """@echo off
:: Runs a quick Windows Defender scan using MpCmdRun.exe
echo Initiating Windows Defender Quick Scan...
"%ProgramFiles%\\Windows Defender\\MpCmdRun.exe" -Scan -ScanType 1
echo Scan complete.
pause""",

    "21_firewall_status_check.bat": """@echo off
:: Checks the status of the Windows Firewall profiles.
echo Checking Windows Firewall status...
netsh advfirewall show allprofiles state
pause""",

    "22_check_password_policy.bat": """@echo off
:: Displays the current account password policy.
echo Checking password policy...
net accounts
pause""",

    "23_export_installed_software.bat": """@echo off
:: Exports a list of installed software to a text file using WMIC.
echo Exporting installed software list to software_list.txt...
wmic product get name,version > software_list.txt
echo Done.
pause""",

    "24_show_hidden_files.bat": """@echo off
:: Toggles showing hidden files in Explorer.
echo This script demonstrates how to toggle hidden files (registry edit required).
echo Currently, it just lists hidden files in the C: drive root as a safe alternative:
dir C:\\ /a:h
pause""",

    # System & Utility
    "25_export_system_drivers.bat": """@echo off
:: Exports a list of installed drivers.
echo Exporting driver list to drivers.txt...
driverquery > drivers.txt
echo Done.
pause""",

    "26_generate_battery_report.bat": """@echo off
:: Generates a Windows battery report (for laptops).
echo Generating battery report...
powercfg /batteryreport /output "battery_report.html"
echo Report saved to battery_report.html
pause""",

    "27_network_troubleshooter.bat": """@echo off
:: Runs basic network troubleshooting commands.
echo Pinging Google DNS...
ping 8.8.8.8
echo.
echo Tracing route to Google DNS...
tracert -d -h 5 8.8.8.8
pause""",

    "28_clear_windows_update_cache.bat": """@echo off
:: Safely stops Windows Update service and clears the SoftwareDistribution folder (requires Admin).
echo Note: Run as Administrator!
echo Stopping Windows Update service...
net stop wuauserv
echo Clearing update cache...
del /f /q /s %windir%\\SoftwareDistribution\\Download\\*.*
echo Starting Windows Update service...
net start wuauserv
pause""",

    "29_restart_explorer.bat": """@echo off
:: Restarts the Windows Explorer process safely.
echo Restarting Windows Explorer...
taskkill /f /im explorer.exe
start explorer.exe
echo Explorer restarted.
pause""",

    "30_repair_corrupt_system_files.bat": """@echo off
:: Runs System File Checker (requires Admin).
echo Note: Run as Administrator!
echo Starting System File Checker...
sfc /scannow
pause"""
}

os.makedirs(r"e:\Batch Scrippting\sample_scripts", exist_ok=True)
for name, content in scripts.items():
    with open(os.path.join(r"e:\Batch Scrippting\sample_scripts", name), "w", encoding="utf-8") as f:
        f.write(content)

print("Generated 20 scripts successfully.")
