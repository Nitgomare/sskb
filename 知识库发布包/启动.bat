@echo off
cd /d "%~dp0"

set "PYTHON_EXE=%~dp0runtime\python.exe"
set "URL=http://127.0.0.1:8000/"

if not exist "%PYTHON_EXE%" (
    echo ERROR: runtime\python.exe was not found.
    pause
    exit /b 1
)

if not exist "site\index.html" (
    echo ERROR: site\index.html was not found.
    pause
    exit /b 1
)

echo ==========================================
echo Knowledge base is starting...
echo.
echo %URL%
echo.
echo Keep this window open.
echo Press Ctrl+C to stop.
echo ==========================================

start "" "%URL%"

"%PYTHON_EXE%" -m http.server 8000 --bind 127.0.0.1 --directory "%~dp0site"

pause