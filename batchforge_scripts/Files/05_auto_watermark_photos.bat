@echo off
:: ============================================================
:: AUTO-WATERMARK PHOTOS WITH TIMESTAMP
:: Stamps every JPG/PNG with a visible date-time watermark
:: using PowerShell and System.Drawing. No external tools.
:: ============================================================
set "FOLDER=C:\Photos"
echo Watermarking images in %FOLDER%...
powershell -NoProfile -Command ^
"Add-Type -AssemblyName System.Drawing; ^
Get-ChildItem '%FOLDER%' -Include *.jpg,*.png -Recurse | ForEach-Object { ^
    $img=[System.Drawing.Image]::FromFile($_.FullName); ^
    $g=[System.Drawing.Graphics]::FromImage($img); ^
    $font=New-Object System.Drawing.Font('Arial',18,[System.Drawing.FontStyle]::Bold); ^
    $brush=New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White); ^
    $g.DrawString((Get-Date -Format 'yyyy-MM-dd HH:mm'),$font,$brush,10,10); ^
    $img.Save($_.FullName); $g.Dispose(); $img.Dispose() }"
echo Done. All images watermarked.
