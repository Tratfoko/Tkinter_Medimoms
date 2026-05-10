# 🔐 Login Backend - Complete Guide

## 📁 Backend File Locations

```
medimoms_desktop/
│
├── 📂 database/                          # DATABASE LAYER
│   ├── connection.py                    # ⭐ MySQL connection pool
│   └── queries/
│       └── user_queries.py              # ⭐ User SQL queries
│
├── 📂 services/                          # BUSINESS LOGIC LAYER
│   └── auth_service.py                  # ⭐ Authentication logic
│
├── 📂 utils/                             # UTILITIES
│   └── validators.py                    # ⭐ Input validation
│
├── 📂 ui/                                # FRONTEND LAYER
│   └── auth/
│       └── login_window.py              # ⭐ Login UI
│
├── config.py                             # ⭐ Database configuration
└── main.py                               # ⭐ Application entry point
```

## 🔄 Complete Login Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    USER ENTERS CREDENTIALS                   │
│                  (username/email + password)                 │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  1. FRONTEND (ui/auth/login_window.py)                      │
│     - User clicks "🚀 Sign In" button                       │
│     - handle_login() method called                          │
│     - Gets username and password from input fields          │
│     - Basic validation (not empty)                          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  2. SERVICE LAYER (services/auth_service.py)                │
│     - authenticate_user(username, password) called          │
│     - Sanitizes input                                       │
│     - Calls database to get user                            │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  3. DATABASE LAYER (database/queries/user_queries.py)       │
│     - get_user_by_username_or_email() called                │
│     - Executes SQL query                                    │
│     - Returns user data or None                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  4. DATABASE CONNECTION (database/connection.py)            │
│     - get_connection() gets connection from pool            │
│     - Executes query on MySQL database                      │
│     - Returns results                                       │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  5. BACK TO SERVICE LAYER (services/auth_service.py)        │
│     - Checks account status (pending/approved/rejected)     │
│     - Verifies password with bcrypt                         │
│     - Updates last_login timestamp                          │
│     - Gets user's barangays                                 │
│     - Builds user session data                              │
│     - Returns (True, user_data) or (False, error_message)   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  6. BACK TO FRONTEND (ui/auth/login_window.py)              │
│     - Receives result from authenticate_user()              │
│     - If success: Shows success message, calls callback     │
│     - If failed: Shows error message, clears password       │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  7. MAIN APPLICATION (main.py)                              │
│     - on_login_success() callback triggered                 │
│     - Stores user data in session                           │
│     - Shows dashboard based on user role                    │
└─────────────────────────────────────────────────────────────┘
```

## 📄 Backend Files Explained

### 1. 📄 `database/connection.py` - Database Connection Pool

**Purpose**: Manages MySQL database connections efficiently

**Key Functions:**
```python
init_connection_pool()    # Initialize connection pool (5 connections)
get_connection()          # Get a connection from the pool
test_connection()         # Test if database is working
```

**Code:**
```python
import mysql.connector
from mysql.connector import pooling
from config import DB_CONFIG

connection_pool = None

def init_connection_pool():
    """Initialize MySQL connection pool"""
    global connection_pool
    connection_pool = pooling.MySQLConnectionPool(
        pool_name="medimoms_pool",
        pool_size=5,
        pool_reset_session=True,
        **DB_CONFIG
    )
    return True

def get_connection():
    """Get a connection from the pool"""
    return connection_pool.get_connection()
```

**Used by**: All database query files

---

### 2. 📄 `database/queries/user_queries.py` - User Database Queries

**Purpose**: All SQL queries related to users table

**Key Functions:**
```python
get_user_by_username_or_email(username_or_email)  # Get user record
update_last_login(user_id)                        # Update login time
get_user_barangays(user_id)                       # Get assigned barangays
```

**Code:**
```python
from database.connection import get_connection

def get_user_by_username_or_email(username_or_email: str):
    """Get user by username or email"""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """
        SELECT id, first_name, middle_name, last_name, username, email, 
               password, role, status, contact_number, created_at, last_login
        FROM users 
        WHERE (username = %s OR email = %s)
    """
    
    cursor.execute(query, (username_or_email, username_or_email))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return user
```

**SQL Query Executed:**
```sql
SELECT id, first_name, middle_name, last_name, username, email, 
       password, role, status, contact_number, created_at, last_login
FROM users 
WHERE (username = ? OR email = ?)
```

**Used by**: `services/auth_service.py`

---

### 3. 📄 `services/auth_service.py` - Authentication Business Logic

**Purpose**: Handles all authentication logic and validation

**Key Functions:**
```python
authenticate_user(username, password)    # Main authentication function
verify_password(plain, hashed)           # Verify bcrypt password
build_user_session(user)                 # Build session data
hash_password(password)                  # Hash password with bcrypt
```

**Code:**
```python
import bcrypt
from database.queries.user_queries import (
    get_user_by_username_or_email, 
    update_last_login, 
    get_user_barangays
)
from utils.validators import sanitize_input

def authenticate_user(username_or_email: str, password: str):
    """Authenticate user with username/email and password"""
    
    # 1. Sanitize input
    username_or_email = sanitize_input(username_or_email)
    
    # 2. Get user from database
    user = get_user_by_username_or_email(username_or_email)
    
    if not user:
        return False, "Invalid username or password"
    
    # 3. Check account status
    if user['status'] == 'pending':
        return False, "Your account is pending approval"
    elif user['status'] != 'approved':
        return False, "Invalid account status"
    
    # 4. Verify password
    if not verify_password(password, user['password']):
        return False, "Invalid username or password"
    
    # 5. Update last login
    update_last_login(user['id'])
    
    # 6. Build user session
    user_data = build_user_session(user)
    
    return True, user_data

def verify_password(plain_password: str, hashed_password: str):
    """Verify password against bcrypt hash"""
    # Handle Laravel format ($2y$) to Python format ($2b$)
    if hashed_password.startswith('$2y$'):
        hashed_password = '$2b$' + hashed_password[4:]
    
    return bcrypt.checkpw(
        plain_password.encode('utf-8'), 
        hashed_password.encode('utf-8')
    )

def build_user_session(user: dict):
    """Build user session data"""
    # Build full name
    full_name = user['first_name']
    if user.get('middle_name'):
        full_name += f" {user['middle_name']}"
    full_name += f" {user['last_name']}"
    
    # Get barangays
    barangays = get_user_barangays(user['id'])
    
    return {
        'id': user['id'],
        'username': user['username'],
        'email': user['email'],
        'full_name': full_name,
        'first_name': user['first_name'],
        'middle_name': user.get('middle_name'),
        'last_name': user['last_name'],
        'role': user['role'],
        'status': user['status'],
        'contact_number': user.get('contact_number'),
        'barangays': barangays
    }
```

**Used by**: `ui/auth/login_window.py`

---

### 4. 📄 `utils/validators.py` - Input Validation

**Purpose**: Validate and sanitize user input

**Key Functions:**
```python
sanitize_input(text)           # Clean user input
validate_email(email)          # Validate email format
validate_username(username)    # Validate username format
validate_password(password)    # Validate password strength
```

**Code:**
```python
import re

def sanitize_input(text: str) -> str:
    """Sanitize user input"""
    if not text:
        return ""
    return text.strip()

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

**Used by**: `services/auth_service.py`

---

### 5. 📄 `ui/auth/login_window.py` - Login Frontend

**Purpose**: User interface for login

**Key Methods:**
```python
create_widgets()              # Build UI components
handle_login()                # Handle login button click
toggle_password_visibility()  # Show/hide password
show_forgot_password()        # Show forgot password dialog
```

**Code:**
```python
import customtkinter as ctk
from tkinter import messagebox
from services.auth_service import authenticate_user

class LoginWindow(ctk.CTkFrame):
    def handle_login(self):
        """Handle login button click"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        # Validation
        if not username:
            messagebox.showerror("Error", "Please enter username")
            return
        
        if not password:
            messagebox.showerror("Error", "Please enter password")
            return
        
        # Disable button
        self.login_btn.configure(state="disabled", text="Signing in...")
        self.update()
        
        # Authenticate
        success, result = authenticate_user(username, password)
        
        if success:
            messagebox.showinfo("Success", f"Welcome {result['full_name']}!")
            self.on_login_success(result)
        else:
            messagebox.showerror("Login Failed", result)
            self.login_btn.configure(state="normal", text="🚀 Sign In")
            self.password_entry.delete(0, 'end')
```

**Used by**: `main.py`

---

### 6. 📄 `config.py` - Database Configuration

**Purpose**: Store database connection settings

**Code:**
```python
import os

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'database': os.getenv('DB_NAME', 'medimoms_system'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', '4110')
}

COLORS = {
    'accent': '#10B981',
    'success': '#10B981',
    'danger': '#EF4444',
    'warning': '#F59E0B',
    'background': '#ECFDF5',
    'text': '#0F172A',
    'text_secondary': '#64748B'
}
```

**Used by**: `database/connection.py`, `ui/` files

---

### 7. 📄 `main.py` - Application Entry Point

**Purpose**: Initialize app and handle login success

**Code:**
```python
import customtkinter as ctk
from database.connection import init_connection_pool, test_connection
from ui.auth.login_window import LoginWindow

class MediMomsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("MediMoms")
        self.geometry("1200x700")
        
        # Initialize database
        init_connection_pool()
        test_connection()
        
        # Show login
        self.show_login()
    
    def show_login(self):
        """Show login window"""
        for widget in self.winfo_children():
            widget.destroy()
        
        login_frame = LoginWindow(
            self, 
            self.on_login_success, 
            self.show_register
        )
    
    def on_login_success(self, user_data):
        """Handle successful login"""
        self.current_user = user_data
        print(f"User logged in: {user_data['full_name']}")
        self.show_dashboard()
    
    def show_dashboard(self):
        """Show dashboard based on user role"""
        # Clear window
        for widget in self.winfo_children():
            widget.destroy()
        
        # Show welcome screen
        welcome_label = ctk.CTkLabel(
            self,
            text=f"Welcome, {self.current_user['full_name']}!",
            font=("Segoe UI", 32, "bold")
        )
        welcome_label.pack(pady=100)

if __name__ == "__main__":
    app = MediMomsApp()
    app.mainloop()
```

---

## 🔐 Security Features

### 1. Password Hashing (Bcrypt)
```python
# When user registers
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# When user logs in
bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
```

### 2. SQL Injection Prevention
```python
# ✅ SAFE - Parameterized query
query = "SELECT * FROM users WHERE username = %s"
cursor.execute(query, (username,))

# ❌ UNSAFE - String concatenation
query = f"SELECT * FROM users WHERE username = '{username}'"  # DON'T DO THIS!
```

### 3. Input Sanitization
```python
username = sanitize_input(username)  # Removes whitespace, cleans input
```

### 4. Account Status Validation
```python
if user['status'] == 'pending':
    return False, "Account pending approval"
elif user['status'] != 'approved':
    return False, "Invalid account status"
```

---

## 📊 Database Tables Used

### users table
```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100),
    middle_name VARCHAR(100),
    last_name VARCHAR(100),
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),  -- bcrypt hash
    role ENUM('admin', 'midwife'),
    status ENUM('pending', 'approved', 'rejected', 'inactive'),
    contact_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL
);
```

### user_barangays table
```sql
CREATE TABLE user_barangays (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    barangay_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (barangay_id) REFERENCES barangays(id)
);
```

---

## 🎯 Quick Reference

### To modify login logic:
- **Change UI**: Edit `ui/auth/login_window.py`
- **Change validation**: Edit `services/auth_service.py`
- **Change SQL queries**: Edit `database/queries/user_queries.py`
- **Change database config**: Edit `config.py` or `.env`

### To debug login issues:
1. Check database connection: `database/connection.py`
2. Check SQL query: `database/queries/user_queries.py`
3. Check authentication logic: `services/auth_service.py`
4. Check UI handling: `ui/auth/login_window.py`

### To add new features:
1. Add SQL query in `database/queries/`
2. Add business logic in `services/`
3. Add UI in `ui/`
4. Follow the same pattern!

---

**All backend code for login is clean, secure, and well-organized!** 🔐
