@echo off
setlocal

cd /d "%~dp0backend"
set ANTHROPIC_API_KEY=placeholder

echo Starting backend at http://127.0.0.1:5000
call .\.venv\Scripts\python.exe app.py
