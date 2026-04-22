@echo off
setlocal

cd /d "%~dp0frontend"

echo Starting frontend at http://127.0.0.1:8000
call ..\backend\.venv\Scripts\python.exe -m http.server 8000
