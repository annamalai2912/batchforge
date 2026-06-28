BatchForge Script Collection
=============================
By Rocky's Lab (techknots.in) | Annamalai K M
40 advanced Windows batch scripts | v1.0

FOLDER STRUCTURE
----------------
Files\      (7 scripts) - Smart sorting, backup, duplicates, watermark, logs
Monitor\    (4 scripts) - Live CPU/RAM dashboard, disk SMART, event log scanner
System\     (6 scripts) - Zombie killer, RAM flush, service watchdog, registry cleaner
Security\   (6 scripts) - USB audit, firewall snapshot, brute-force detector, BitLocker
Network\    (4 scripts) - Packet loss tester, Wi-Fi passwords, LAN scanner, bandwidth
Dev\        (5 scripts) - Auto git push, dependency updater, dead code finder
Repair\     (3 scripts) - Printer unsticker, SFC+DISM healer, adapter reset
Power\      (5 scripts) - Self-destruct, remote cmd, Hyper-V snapshots, power plans

HOW TO USE
----------
1. Open any .bat file in Notepad to review and customise it
2. Edit paths (look for lines with SET "FOLDER=..." or SET "ROOT=...")
3. Right-click > Run as administrator for scripts marked "Run as Admin"
4. Or load into BatchForge app for managed scheduling and execution

SCRIPTS THAT REQUIRE ADMINISTRATOR
------------------------------------
- 13_ram_dns_winsock_refresh.bat
- 14_service_health_watchdog.bat
- 16_deep_temp_cleaner.bat
- 20_brute_force_detector.bat
- 21_bitlocker_audit.bat
- 33_printer_queue_unsticker.bat
- 34_corrupt_system_file_healer.bat
- 35_network_adapter_reset.bat
- 36_self_destructing_script.bat
- 38_hyperv_snapshot_automator.bat
- 39_power_plan_switcher.bat

IMPORTANT
---------
Review each script before running. Some scripts move, delete, or modify
files. Test on non-critical data first. The author is not responsible
for unintended data loss.

