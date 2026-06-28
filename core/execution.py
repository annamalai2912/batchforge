import os
import tempfile
import subprocess
from PyQt6.QtCore import QThread, pyqtSignal


class ScriptExecutionThread(QThread):
    output_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(int)

    def __init__(self, script_content):
        super().__init__()
        self.script_content = script_content
        self.process = None

    def run(self):
        # Create a temporary batch file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".bat", mode='w', encoding='utf-8') as temp_file:
            temp_file.write(self.script_content)
            temp_file_path = temp_file.name

        try:
            self.process = subprocess.Popen(
                ["cmd.exe", "/c", temp_file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            # Read output line by line
            for line in iter(self.process.stdout.readline, ''):
                if line:
                    self.output_signal.emit(line.strip())

            self.process.stdout.close()
            self.process.wait()

            # Emit the return code
            self.finished_signal.emit(self.process.returncode)

        except Exception as e:
            self.output_signal.emit(f"Execution error: {str(e)}")
            self.finished_signal.emit(-1)
        finally:
            # Clean up temporary file
            try:
                os.remove(temp_file_path)
            except OSError:
                pass

    def stop(self):
        if self.process:
            try:
                subprocess.run(['taskkill', '/F', '/T', '/PID', str(self.process.pid)], 
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                               creationflags=subprocess.CREATE_NO_WINDOW)
            except Exception:
                self.process.terminate()
