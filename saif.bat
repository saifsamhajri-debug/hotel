@echo off
cd /d D:\hotel(1)
start "" ".venv\Scripts\python.exe" run.py
timeout /t 3 >nul
start http://127.0.0.1:5000
exit
