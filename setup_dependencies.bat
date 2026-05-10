@echo off
echo ========================================
echo MediMoms Desktop - Setup Script
echo ========================================
echo.

echo [1/3] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)
echo.

echo [2/3] Installing required packages...
echo This may take a few minutes...
echo.

cd medimoms_desktop
pip install customtkinter==5.2.1
pip install mysql-connector-python==8.2.0
pip install bcrypt==4.1.2
pip install pydantic==2.5.3
pip install python-dateutil==2.8.2

echo.
echo [3/3] Verifying installation...
python -c "import customtkinter; print('✓ customtkinter installed')"
python -c "import mysql.connector; print('✓ mysql-connector-python installed')"
python -c "import bcrypt; print('✓ bcrypt installed')"
python -c "import pydantic; print('✓ pydantic installed')"
python -c "import dateutil; print('✓ python-dateutil installed')"

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo You can now run the application with:
echo   cd medimoms_desktop
echo   python main.py
echo.
pause
