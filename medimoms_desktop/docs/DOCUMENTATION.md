# MediMoms Desktop Application - Complete Guide

## 📚 Table of Contents
1. [Quick Start](#quick-start)
2. [Project Structure](#project-structure)
3. [Backend Architecture](#backend-architecture)
4. [Design System](#design-system)
5. [Features](#features)
6. [Database Connection](#database-connection)
7. [How to Add New Features](#how-to-add-new-features)

---

## 🚀 Quick Start

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Configure database (edit .env or config.py)
DB_HOST=localhost
DB_NAME=medimoms_system
DB_USER=root
DB_PASSWORD=your_password

# Run application
python main.py
```

### Test Dependencies
```bash
python test_dependencies.py
```

---

## 📁 Project Structure

```
medimoms_desktop/
├── main.py                    # Application entry point
├── config.py                  # Configuration & database settings
├── .env                       # Environment variables
│
├── database/                  # DATABASE LAYER
│   ├── connection.py         # MySQL connection pool
│   └── queries/              # SQL queries by module
│       ├── user_queries.py
│       └── registration_queries.py
│
├── services/                  # BUSINESS LOGIC LAYER
│   ├── auth_service.py       # Authentication logic
│   └── registration_service.py
│
├── ui/                        # PRESENTATION LAYER
│   ├── auth/
│   │   ├── login_window.py   # Login screen
│   │   └── register_window.py # Registration screen
│   └── components/           # Reusable UI components
│
└── utils/                     # UTILITIES
    └── validators.py         # Input validation
```

---

## 🏗️ Backend Architecture

### Layer Separation (MVC Pattern)

```
UI Layer (ui/)
    ↓ calls
Service Layer (services/)
    ↓ calls
Database Layer (database/queries/)
    ↓ queries
MySQL Database
```

### Rules
- **UI Layer**: Only display and user interaction
- **Service Layer**: Business logic and validation
- **Database Layer**: Raw SQL queries only
- **Never skip layers**: Always UI → Service → Database

### Example Flow

```python
# UI Layer (login_window.py)
def handle_login(self):
    username = self.username_entry.get()
    password = self.password_entry.get()
    success, result = authenticate_user(username, password)  # Call service

# Service Layer (auth_service.py)
def authenticate_user(username, password):
    user = get_user_by_username_or_email(username)  # Call database
    if verify_password(password, user['password']):
        return True, build_user_session(user)

# Database Layer (user_queries.py)
def get_user_by_username_or_email(username):
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    return cursor.fetchone()
```

---

## 🎨 Design System

### Color Palette
```
PRIMARY (Emerald Green - Healthcare Theme)
#10B981  Main emerald (buttons, accents)
#059669  Dark emerald (hover states)
#D1FAE5  Light emerald (backgrounds)
#ECFDF5  Very light emerald (page background)

NEUTRAL (Slate - Professional)
#0F172A  Dark slate (primary text)
#64748B  Medium slate (secondary text)
#94A3B8  Light slate (placeholders)
#E2E8F0  Border color
#FFFFFF  White (cards, inputs)

SEMANTIC
#10B981  Success (emerald)
#F59E0B  Warning (amber)
#EF4444  Danger (red)
```

### Typography
```
Font: "Segoe UI"
Title: 32px bold
Section: 16px bold
Labels: 12-13px bold
Body: 13-14px regular
Buttons: 14-15px bold
```

### Component Sizes
```
Cards: 480-600px width, 24px radius
Inputs: 45-50px height, 10-12px radius
Buttons: 50-54px height, 10-12px radius
Padding: 40-50px for cards
Spacing: 15-20px between elements
```

### Usage Example
```python
# Primary Button
ctk.CTkButton(
    text="Sign In",
    height=54,
    font=("Segoe UI", 15, "bold"),
    fg_color="#10B981",
    hover_color="#059669",
    corner_radius=12
)

# Input Field
ctk.CTkEntry(
    height=50,
    font=("Segoe UI", 14),
    border_width=2,
    corner_radius=12,
    border_color="#E2E8F0",
    fg_color="white",
    text_color="#0F172A"
)
```

---

## ✨ Features

### 1. Login System
- Username or email login
- Password visibility toggle
- Remember me option
- Forgot password link
- Account status validation (pending/approved/rejected/inactive)
- Bcrypt password verification
- Session management

### 2. Registration System
- Self-service midwife registration
- Personal information (name, contact)
- Account creation (username, email, password)
- Barangay assignment (multi-select)
- Complete validation:
  - Username format (3-50 chars, alphanumeric)
  - Email format (regex)
  - Password strength (min 6 chars)
  - Password confirmation
  - Duplicate prevention
- Pending approval workflow
- Bcrypt password hashing

### 3. Security Features
- ✅ Bcrypt password hashing
- ✅ SQL injection prevention (parameterized queries)
- ✅ Input sanitization
- ✅ Connection pooling
- ✅ Account status validation
- ✅ Duplicate username/email prevention

---

## 🔌 Database Connection

### Configuration
Database settings are in `config.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'database': 'medimoms_system',
    'user': 'root',
    'password': '4110'
}
```

Or use `.env` file:
```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=medimoms_system
DB_USER=root
DB_PASSWORD=4110
```

### Connection Flow
```
main.py
  ↓ init_connection_pool()
database/connection.py
  ↓ creates pool (5 connections)
MySQL Connection Pool
  ↓ get_connection()
database/queries/*.py
  ↓ execute queries
MySQL Database
```

### Functions
```python
init_connection_pool()  # Initialize pool on startup
get_connection()        # Get connection from pool
test_connection()       # Test database connectivity
```

---

## 🔧 How to Add New Features

### Step 1: Create Database Queries
**File**: `database/queries/feature_queries.py`
```python
from database.connection import get_connection

def get_all_records():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM table_name"
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records
```

### Step 2: Create Service
**File**: `services/feature_service.py`
```python
from database.queries.feature_queries import get_all_records

def fetch_records():
    records = get_all_records()
    # Apply business logic here
    return records
```

### Step 3: Create UI
**File**: `ui/feature_window.py`
```python
import customtkinter as ctk
from services.feature_service import fetch_records

class FeatureWindow(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
    
    def create_widgets(self):
        # Create UI components
        pass
    
    def load_data(self):
        records = fetch_records()
        # Display records
```

### Step 4: Follow Design System
- Use emerald green theme (#10B981)
- Use Segoe UI font
- Follow spacing guidelines (40-50px padding)
- Use consistent component sizes
- Add hover states and transitions

---

## 📊 Database Schema

### users table
```sql
id              INT PRIMARY KEY AUTO_INCREMENT
first_name      VARCHAR(100)
middle_name     VARCHAR(100) NULL
last_name       VARCHAR(100)
username        VARCHAR(50) UNIQUE
email           VARCHAR(100) UNIQUE
password        VARCHAR(255)  -- bcrypt hash
contact_number  VARCHAR(20) NULL
role            ENUM('admin', 'midwife')
status          ENUM('pending', 'approved', 'rejected', 'inactive')
created_at      TIMESTAMP
last_login      TIMESTAMP NULL
```

### user_barangays table
```sql
id              INT PRIMARY KEY AUTO_INCREMENT
user_id         INT FOREIGN KEY → users(id)
barangay_id     INT FOREIGN KEY → barangays(id)
```

### barangays table
```sql
id              INT PRIMARY KEY AUTO_INCREMENT
name            VARCHAR(100)
```

---

## 🎯 Best Practices

### Code Quality
- ✅ Use type hints
- ✅ Add docstrings to functions
- ✅ Handle exceptions properly
- ✅ Close database connections
- ✅ Use parameterized queries
- ✅ Sanitize user input
- ✅ Follow layer separation

### Security
- ✅ Never store plain text passwords
- ✅ Always use bcrypt for hashing
- ✅ Validate all user input
- ✅ Use parameterized queries
- ✅ Sanitize inputs before database operations
- ✅ Check account status before allowing access

### UI/UX
- ✅ Provide clear error messages
- ✅ Show loading states
- ✅ Use consistent styling
- ✅ Add keyboard shortcuts
- ✅ Auto-focus on first field
- ✅ Validate before submission
- ✅ Give user feedback

---

## 🐛 Troubleshooting

### Database Connection Failed
```
Check:
1. MySQL server is running
2. Database credentials in config.py
3. Database 'medimoms_system' exists
4. User has proper permissions
```

### Import Errors
```
Run: pip install -r requirements.txt
Or: python test_dependencies.py
```

### Login Not Working
```
Check:
1. User exists in database
2. User status is 'approved'
3. Password is correct
4. Database connection is working
```

### Registration Not Working
```
Check:
1. All required fields filled
2. Username/email not already taken
3. Password meets requirements
4. At least one barangay selected
5. Database connection is working
```

---

## 📝 Development Workflow

### Adding a New Screen
1. Create query file in `database/queries/`
2. Create service file in `services/`
3. Create UI file in `ui/`
4. Follow design system guidelines
5. Test thoroughly
6. Update this documentation

### Testing Checklist
- [ ] All required fields validated
- [ ] Error messages clear and helpful
- [ ] Success messages shown
- [ ] Database operations work
- [ ] UI is responsive
- [ ] Keyboard shortcuts work
- [ ] Loading states shown
- [ ] Back/cancel buttons work

---

## 🎓 Key Concepts

### MVC Architecture
- **Model** (Database Layer): Data access
- **View** (UI Layer): User interface
- **Controller** (Service Layer): Business logic

### Connection Pooling
- Maintains 5 active connections
- Reuses connections efficiently
- Prevents connection exhaustion
- Improves performance

### Password Security
- Bcrypt hashing (one-way encryption)
- Salt automatically generated
- Handles Laravel format ($2y$) and Python format ($2b$)
- Never store or log plain text passwords

### Input Validation
- Client-side (UI) - Fast feedback
- Server-side (Service) - Security
- Database constraints - Last line of defense

---

## 📞 Support

### Common Issues
1. **Can't login**: Check account status (must be 'approved')
2. **Registration fails**: Check username/email uniqueness
3. **Database error**: Verify connection settings
4. **Import error**: Install dependencies

### File Locations
- **Database config**: `config.py` or `.env`
- **Connection pool**: `database/connection.py`
- **User queries**: `database/queries/user_queries.py`
- **Auth logic**: `services/auth_service.py`
- **Login UI**: `ui/auth/login_window.py`

---

## 🚀 Next Steps

### Recommended Features to Build
1. **Dashboard** - Stats cards, charts, recent activity
2. **Immunization Records** - CRUD operations
3. **Maternal Care** - Prenatal visits tracking
4. **Family Planning** - Client management
5. **Senior Citizens** - Health monitoring
6. **Admin Panel** - User approval, barangay management
7. **Reports** - Export to Excel/PDF
8. **Appointments** - Scheduling system

### Follow This Pattern
For each feature:
1. Create `database/queries/feature_queries.py`
2. Create `services/feature_service.py`
3. Create `ui/feature_window.py`
4. Use design system colors and components
5. Add validation and error handling
6. Test thoroughly

---

**This is your complete reference guide. Keep it updated as you add new features!** 📚
