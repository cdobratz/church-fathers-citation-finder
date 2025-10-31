@echo off
REM Church Fathers MVP - Quick Start Script (Windows)

echo ==========================================
echo Church Fathers MVP - Quick Setup
echo ==========================================
echo.

REM Check if we're in the right directory
if not exist "README.md" (
    echo Error: Please run this script from the project root directory
    exit /b 1
)

echo Setting up Backend...
echo.

REM Backend setup
cd backend

REM Check if venv exists
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)

REM Activate venv
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing Python dependencies...
pip install -r requirements.txt --quiet

REM Copy env file if it doesn't exist
if not exist ".env" (
    echo Creating .env file...
    copy .env.example .env
)

echo Backend setup complete!
echo.

REM Frontend setup
cd ..\frontend

echo Setting up Frontend...
echo.

REM Install npm dependencies
echo Installing Node dependencies (this may take a minute)...
call npm install --silent

REM Copy env file if it doesn't exist
if not exist ".env.local" (
    echo Creating .env.local file...
    copy .env.example .env.local
)

echo Frontend setup complete!
echo.

cd ..

echo ==========================================
echo Setup Complete!
echo ==========================================
echo.
echo To start the application:
echo.
echo 1. Terminal 1 (Backend):
echo    cd backend
echo    venv\Scripts\activate
echo    python run.py
echo.
echo 2. Terminal 2 (Frontend):
echo    cd frontend
echo    npm run dev
echo.
echo 3. Open http://localhost:3000
echo.
echo Happy coding!
echo.

pause
