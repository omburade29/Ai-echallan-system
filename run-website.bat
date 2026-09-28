@echo off
REM One-link website: build React UI, then serve FE+BE together on port 8000.
cd /d "%~dp0"

echo Building frontend...
cd frontend
call npm run build
if errorlevel 1 (
  echo Frontend build failed.
  exit /b 1
)

cd ..\backend
if not exist ".venv\Scripts\python.exe" (
  echo Creating Python venv...
  python -m venv .venv
  call .venv\Scripts\pip.exe install -r requirements.txt
)

echo.
echo Starting website at http://127.0.0.1:8000/
echo.
.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
