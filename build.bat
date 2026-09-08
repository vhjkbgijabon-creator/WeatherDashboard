@echo off
REM ========================================
REM Weather Dashboard - Build to EXE
REM ========================================

chcp 65001 >nul
cls

echo.
echo ╔══════════════════════════════════════════════════════════╗
echo ║         Weather Dashboard - EXE Builder                  ║
echo ║              ساخت فایل Weather Dashboard.exe             ║
echo ╚══════════════════════════════════════════════════════════╝
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not installed or not in PATH
    echo [!] Download Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [✓] Python detected
echo.

REM Install/Update pip
echo [*] Updating pip...
python -m pip install --upgrade pip -q

REM Install requirements
echo [*] Installing required packages...
pip install requests pillow pyinstaller -q

if %errorlevel% neq 0 (
    echo [!] Failed to install requirements
    pause
    exit /b 1
)

echo [✓] All packages installed
echo.

REM Build EXE
echo [*] Building Weather Dashboard.exe...
echo [*] This may take 2-3 minutes...
echo.

pyinstaller ^
    --onefile ^
    --windowed ^
    --name="Weather Dashboard" ^
    --icon=NONE ^
    --add-data ".:." ^
    weather_dashboard_exe.py

if %errorlevel% neq 0 (
    echo.
    echo [!] Build failed!
    pause
    exit /b 1
)

echo.
echo ╔═════��════════════════════════════════════════════════════╗
echo ║                  BUILD SUCCESSFUL!                       ║
echo ║                                                          ║
echo ║  Your executable file:                                  ║
echo ║  dist\Weather Dashboard.exe                             ║
echo ║                                                          ║
echo ║  To run the application:                                ║
echo ║  1. Open the dist folder                               ║
echo ║  2. Double-click "Weather Dashboard.exe"               ║
echo ║  3. Enter a city name and search!                      ║
echo ╚══════════════════════════════════════════════════════════╝
echo.

REM Open dist folder
explorer dist

pause
