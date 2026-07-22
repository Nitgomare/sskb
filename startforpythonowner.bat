from pathlib import Path

content = r'''@echo off
setlocal
title Knowledge Base Server

cd /d "%~dp0"

set "PYTHON_EXE=E:\Anaconda\envs\research_web\python.exe"
set "URL=http://127.0.0.1:8000/"

echo ==================================================
echo Knowledge Base Launcher
echo ==================================================
echo Working directory:
echo %CD%
echo.

if not exist "%PYTHON_EXE%" (
    echo ERROR: Python was not found:
    echo %PYTHON_EXE%
    echo.
    pause
    exit /b 1
)

if not exist "build_all.py" (
    echo ERROR: build_all.py was not found:
    echo %CD%\build_all.py
    echo.
    pause
    exit /b 1
)

echo Python environment:
echo %PYTHON_EXE%
"%PYTHON_EXE%" --version
echo.

echo Building website...
"%PYTHON_EXE%" "%CD%\build_all.py"

if errorlevel 1 (
    echo.
    echo ERROR: Website build failed.
    echo.
    pause
    exit /b 1
)

if not exist "site\index.html" (
    echo.
    echo ERROR: site\index.html was not generated.
    echo.
    pause
    exit /b 1
)

echo.
echo ==================================================
echo Website address:
echo %URL%
echo.
echo Keep this window open.
echo Press Ctrl+C to stop the server.
echo ==================================================
echo.

REM Open the local address with the default browser.
REM No PowerShell and no hidden process are used.
start "" "%URL%"

REM Run the local HTTP server in this visible window.
"%PYTHON_EXE%" -m http.server 8000 --bind 127.0.0.1 --directory "%CD%\site"

echo.
echo Server stopped.
pause
endlocal
'''

path = Path("/mnt/data/start_knowledge_base_safe.cmd")
path.write_text(content, encoding="ascii")
print(path)