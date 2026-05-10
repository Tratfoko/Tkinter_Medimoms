# Quick Start Guide - MediMoms Desktop

## Fix "customtkinter" Error

If you get an error about `customtkinter` not being found, follow these steps:

### Option 1: Run the Setup Script (Easiest)

1. Double-click `setup_dependencies.bat` in the project root folder
2. Wait for all packages to install
3. Run the application

### Option 2: Manual Installation

Open Command Prompt or PowerShell and run:

```bash
# Navigate to the project folder
cd "c:\Users\tetek\Desktop\Medimoms Tkinter\medimoms_desktop"

# Install all dependencies
pip install -r requirements.txt
```

### Option 3: Install Packages One by One

If the above doesn't work, install each package individually:

```bash
pip install customtkinter
pip install mysql-connector-python
pip install bcrypt
pip install pydantic
pip install python-dateutil
```

## Common Issues

### Issue: "pip is not recognized"

**Solution:** Add Python to your PATH or use:
```bash
python -m pip install customtkinter
```

### Issue: "Permission denied"

**Solution:** Run Command Prompt as Administrator or use:
```bash
pip install --user customtkinter
```

### Issue: "No module named 'customtkinter'"

**Solution:** Make sure you're using the correct Python version:
```bash
python --version  # Should be 3.8 or higher
pip --version     # Should match your Python version
```

## Running the Application

After installing dependencies:

```bash
cd medimoms_desktop
python main.py
```

## Test Login Credentials

Use any existing user from your database:

**Example Admin:**
- Username: `admin`
- Password: (your admin password)

**Example Midwife:**
- Username: (any approved midwife username)
- Password: (their password)

## Need Help?

1. Make sure MySQL server is running
2. Verify database credentials in `config.py`
3. Check that `medimoms_system` database exists
4. Ensure Python 3.8+ is installed

## Verification

To verify everything is installed correctly:

```bash
python -c "import customtkinter; print('✓ CustomTkinter OK')"
python -c "import mysql.connector; print('✓ MySQL Connector OK')"
python -c "import bcrypt; print('✓ Bcrypt OK')"
```

If all three print "OK", you're ready to run the application!
