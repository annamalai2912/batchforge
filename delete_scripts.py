import shutil
import os

path = r"e:\Batch Scrippting\batchforge_scripts\Automation"
if os.path.exists(path):
    shutil.rmtree(path)
    print("Deleted successfully.")
else:
    print("Path does not exist.")
