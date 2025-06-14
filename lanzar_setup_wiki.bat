@echo off
SETLOCAL

REM Ruta del proyecto
set "SCRIPT_PATH=%~dp0setup_wiki.ps1"

REM Comprobar que PowerShell esté disponible
where powershell >nul 2>&1
if errorlevel 1 (
    echo ❌ PowerShell no está disponible en este sistema.
    pause
    exit /b 1
)

REM Ejecutar el script .ps1 en nueva ventana PowerShell con permisos
powershell.exe -NoExit -ExecutionPolicy Bypass -File "%SCRIPT_PATH%"

ENDLOCAL
