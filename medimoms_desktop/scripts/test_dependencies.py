"""
Test script to verify all dependencies are installed correctly
"""

print("=" * 50)
print("MediMoms Desktop - Dependency Check")
print("=" * 50)
print()

# Test imports
tests_passed = 0
tests_failed = 0

# Test 1: CustomTkinter
try:
    import customtkinter as ctk
    print("✓ customtkinter:", ctk.__version__)
    tests_passed += 1
except ImportError as e:
    print("✗ customtkinter: NOT INSTALLED")
    print(f"  Error: {e}")
    tests_failed += 1

# Test 2: MySQL Connector
try:
    import mysql.connector
    print("✓ mysql-connector-python: OK")
    tests_passed += 1
except ImportError as e:
    print("✗ mysql-connector-python: NOT INSTALLED")
    print(f"  Error: {e}")
    tests_failed += 1

# Test 3: Bcrypt
try:
    import bcrypt
    print("✓ bcrypt:", bcrypt.__version__)
    tests_passed += 1
except ImportError as e:
    print("✗ bcrypt: NOT INSTALLED")
    print(f"  Error: {e}")
    tests_failed += 1

# Test 4: Pydantic
try:
    import pydantic
    print("✓ pydantic:", pydantic.__version__)
    tests_passed += 1
except ImportError as e:
    print("✗ pydantic: NOT INSTALLED")
    print(f"  Error: {e}")
    tests_failed += 1

# Test 5: Python-dateutil
try:
    import dateutil
    print("✓ python-dateutil: OK")
    tests_passed += 1
except ImportError as e:
    print("✗ python-dateutil: NOT INSTALLED")
    print(f"  Error: {e}")
    tests_failed += 1

print()
print("=" * 50)
print(f"Results: {tests_passed} passed, {tests_failed} failed")
print("=" * 50)
print()

if tests_failed > 0:
    print("⚠ Some dependencies are missing!")
    print()
    print("To install missing dependencies, run:")
    print("  pip install -r requirements.txt")
    print()
    print("Or run the setup script:")
    print("  setup_dependencies.bat")
else:
    print("✓ All dependencies are installed correctly!")
    print()
    print("You can now run the application:")
    print("  python main.py")

print()
input("Press Enter to exit...")
