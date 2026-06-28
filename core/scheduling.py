import subprocess


class Scheduler:
    @staticmethod
    def create_task(task_name, script_path, trigger_type, trigger_time=None):
        """
        Creates a scheduled task using schtasks.exe
        trigger_type: 'ONCE', 'DAILY', 'WEEKLY', 'MONTHLY', 'ONLOGON', 'ONIDLE'
        trigger_time: 'HH:MM' (required for ONCE, DAILY, WEEKLY, MONTHLY)
        """
        command = [
            "schtasks.exe", "/Create",
            "/TN", f"BatchForge\\{task_name}",
            "/TR", script_path,
            "/SC", trigger_type,
            "/F"  # Force overwrite if exists
        ]

        if trigger_time and trigger_type not in ['ONLOGON', 'ONIDLE']:
            command.extend(["/ST", trigger_time])

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            if result.returncode == 0:
                return True, result.stdout
            else:
                return False, result.stderr
        except Exception as e:
            return False, str(e)

    @staticmethod
    def delete_task(task_name):
        command = [
            "schtasks.exe", "/Delete",
            "/TN", f"BatchForge\\{task_name}",
            "/F"
        ]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            return result.returncode == 0, result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return False, str(e)

    @staticmethod
    def query_task(task_name):
        command = [
            "schtasks.exe", "/Query",
            "/TN", f"BatchForge\\{task_name}",
            "/FO", "LIST"
        ]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            if result.returncode == 0:
                return True, result.stdout
            else:
                return False, "Task not found"
        except Exception as e:
            return False, str(e)
