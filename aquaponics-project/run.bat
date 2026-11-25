@echo off
rem Run a local scenario: run.bat <name>   (run.bat alone lists the runs)
rem Uses the project venv if it exists, else the real Python install, else "python".
setlocal
cd /d "%~dp0"
set "PY=python"
if exist "C:\Users\ajith\AppData\Local\Python\bin\python.exe" set "PY=C:\Users\ajith\AppData\Local\Python\bin\python.exe"
if exist ".venv\Scripts\python.exe" set "PY=.venv\Scripts\python.exe"
"%PY%" run.py %*
endlocal
