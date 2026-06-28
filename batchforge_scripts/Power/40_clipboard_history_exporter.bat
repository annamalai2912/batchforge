@echo off
:: ============================================================
:: CLIPBOARD HISTORY EXPORTER
:: Reads Windows 10/11 clipboard history and exports all
:: saved text entries to a plain text file.
:: Requires Clipboard History enabled in Windows Settings.
:: ============================================================
set "OUT=%TEMP%\clipboard_export.txt"
echo Clipboard History Export > "%OUT%"
echo Date: %date% %time% >> "%OUT%"
echo ========================= >> "%OUT%"
powershell -NoProfile -Command ^
  "Add-Type -AssemblyName Windows.ApplicationModel; ^
   [Windows.ApplicationModel.DataTransfer.Clipboard,Windows.ApplicationModel,ContentType=WindowsRuntime] | Out-Null; ^
   $h=[Windows.ApplicationModel.DataTransfer.Clipboard]::GetHistoryItemsAsync().GetResults(); ^
   foreach($item in $h.Items){ ^
     if($item.Content.Contains('Text')){ ^
       $t=$item.Content.GetTextAsync().GetResults(); ^
       Add-Content '%OUT%' $t; Add-Content '%OUT%' '---' ^
     } ^
   }"
echo Exported: %OUT%
start notepad "%OUT%"
