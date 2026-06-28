@echo off
:: ============================================================
:: SCHEDULED SELF-DESTRUCTING SCRIPT
:: Runs payload once at a specific time, then deletes itself
:: and removes its own scheduled task. Leaves zero traces.
:: ============================================================
set "TASKNAME=SelfDestruct_OneShot"
set "TRIGGER_TIME=23:00"
set "SELF=%~f0"
echo Scheduling self-destruct execution at %TRIGGER_TIME%...
schtasks /create /tn "%TASKNAME%" /tr "cmd /c \"%SELF%\" && schtasks /delete /tn \"%TASKNAME%\" /f && del /f \"%SELF%\"" /sc once /st %TRIGGER_TIME% /f
echo Scheduled. This script will run at %TRIGGER_TIME% then erase itself.
echo.
echo --- YOUR PAYLOAD GOES BELOW THIS LINE ---
echo Hello from the self-destructing script at %time%
echo --- END PAYLOAD ---
