@echo off
:: ============================================================
:: DUPLICATE FILE FINDER WITH MD5 HASH
:: Finds truly identical files by comparing MD5 hashes.
:: Logs all duplicate groups to a report file.
:: ============================================================
set "FOLDER=C:\Users\%USERNAME%\Documents"
set "LOG=%TEMP%\dupes_report.txt"
echo MD5 Duplicate Report > "%LOG%"
echo Folder: %FOLDER% >> "%LOG%"
echo Scanned: %date% %time% >> "%LOG%"
echo ========================= >> "%LOG%"
set "TMP=%TEMP%\hashlist.txt"
if exist "%TMP%" del "%TMP%"
for /r "%FOLDER%" %%F in (*.*) do (
    for /f "skip=1 tokens=*" %%H in ('CertUtil -hashfile "%%F" MD5 2^>nul') do (
        echo %%H  %%F >> "%TMP%"
        goto :next
    )
    :next
)
sort "%TMP%" > "%TEMP%\sorted_hashes.txt"
powershell -NoProfile -Command ^
  "Get-Content '%TEMP%\sorted_hashes.txt' | Group-Object {$_.Split()[0]} | Where-Object Count -gt 1 | ForEach-Object { $_.Group } | Out-File '%LOG%' -Append"
start notepad "%LOG%"
