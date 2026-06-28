!include "MUI2.nsh"

Name "BatchForge"
OutFile "BatchForge_Setup.exe"
InstallDir "$PROGRAMFILES\BatchForge"
RequestExecutionLevel admin
BrandingText "Built by Annamalai K M"

!define MUI_ICON "batchforge.ico"
!define MUI_UNICON "batchforge.ico"

!insertmacro MUI_PAGE_LICENSE "LICENSE.txt"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

Section "BatchForge" SecDummy
  SetOutPath "$INSTDIR"
  File "dist\BatchForge.exe"
  File "LICENSE.txt"
  
  CreateShortcut "$SMPROGRAMS\BatchForge.lnk" "$INSTDIR\BatchForge.exe"
  CreateShortcut "$DESKTOP\BatchForge.lnk" "$INSTDIR\BatchForge.exe"
  
  WriteUninstaller "$INSTDIR\Uninstall.exe"
  
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\BatchForge" "DisplayName" "BatchForge"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\BatchForge" "UninstallString" "$\"$INSTDIR\Uninstall.exe$\""
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\BatchForge" "Publisher" "Annamalai K M"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\BatchForge" "DisplayIcon" "$\"$INSTDIR\BatchForge.exe$\""
SectionEnd

Section "Uninstall"
  Delete "$INSTDIR\BatchForge.exe"
  Delete "$INSTDIR\LICENSE.txt"
  Delete "$INSTDIR\Uninstall.exe"
  RMDir "$INSTDIR"
  
  Delete "$SMPROGRAMS\BatchForge.lnk"
  Delete "$DESKTOP\BatchForge.lnk"
  
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\BatchForge"
SectionEnd
