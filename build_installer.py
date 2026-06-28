import os
import urllib.request
import zipfile
import subprocess

NSIS_URL = "https://downloads.sourceforge.net/project/nsis/NSIS%203/3.08/nsis-3.08.zip"
ZIP_PATH = "nsis.zip"
EXTRACT_DIR = "nsis-3.08"
MAKENSIS = os.path.join(EXTRACT_DIR, "makensis.exe")

if not os.path.exists(MAKENSIS):
    print("Downloading NSIS...")
    urllib.request.urlretrieve(NSIS_URL, ZIP_PATH)
    print("Extracting NSIS...")
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(".")
    os.remove(ZIP_PATH)

print("Running NSIS...")
result = subprocess.run([MAKENSIS, "batchforge_installer.nsi"], capture_output=True, text=True)
print(result.stdout)
if result.returncode != 0:
    print(result.stderr)
else:
    print("Installer built successfully!")
