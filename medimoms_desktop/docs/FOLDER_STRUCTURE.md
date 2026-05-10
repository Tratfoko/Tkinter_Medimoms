# 📁 Folder Structure Guide

## ✨ Clean & Organized Structure

```
medimoms_desktop/
│
├── 📂 database/                    # DATABASE LAYER
│   ├── connection.py              # MySQL connection pool
│   └── queries/                   # SQL query modules
│       ├── __init__.py
│       ├── user_queries.py        # User-related queries
│       └── registration_queries.py # Registration queries
│
├── 📂 services/                    # BUSINESS LOGIC LAYER
│   ├── __init__.py
│   ├── auth_service.py            # Authentication logic
│   └── registration_service.py    # Registration logic
│
├── 📂 ui/                          # USER INTERFACE LAYER
│   ├── __init__.py
│   ├── auth/                      # Authentication screens
│   │   ├── __init__.py
│   │   ├── login_window.py        # Login screen
│   │   └── register_window.py     # Registration screen
│   └── components/                # Reusable UI components
│       └── __init__.py
│
├── 📂 utils/                       # UTILITIES
│   ├── __init__.py
│   └── validators.py              # Input validation functions
│
├── 📂 docs/                        # DOCUMENTATION
│   ├── DOCUMENTATION.md           # Complete guide (READ THIS!)
│   ├── CLEANUP_SUMMARY.md         # Cleanup history
│   └── create_database.sql        # Database schema
│
├── 📂 scripts/                     # UTILITY SCRIPTS
│   └── test_dependencies.py       # Dependency checker
│
├── 📂 assets/                      # RESOURCES
│   └── (images, icons, etc.)
│
├── 📄 main.py                      # Application entry point
├── 📄 config.py                    # Configuration settings
├── 📄 .env                         # Environment variables
├── 📄 requirements.txt             # Python dependencies
└── 📄 README.md                    # Quick start guide
```

## 🎯 Folder Purpose

### Core Application Files (Root Level)
```
main.py              → Start here! Application entry point
config.py            → Database & app configuration
.env                 → Environment variables (DB credentials)
requirements.txt     → Python packages to install
README.md            → Quick start & overview
```

### Code Folders (MVC Architecture)
```
database/            → Data access layer (SQL queries)
services/            → Business logic layer (validation, processing)
ui/                  → User interface layer (screens, components)
utils/               → Helper functions (validation, formatting)
```

### Organization Folders
```
docs/                → All documentation & SQL files
scripts/             → Utility scripts (testing, setup)
assets/              → Images, icons, resources
```

## 📚 Where to Find Things

### Need to...
- **Start the app?** → Run `main.py`
- **Configure database?** → Edit `config.py` or `.env`
- **Learn the system?** → Read `docs/DOCUMENTATION.md`
- **Add a feature?** → Follow pattern: `database/` → `services/` → `ui/`
- **Test dependencies?** → Run `scripts/test_dependencies.py`
- **Create database?** → Use `docs/create_database.sql`

### Working on...
- **Login/Registration?** → `ui/auth/`
- **Database queries?** → `database/queries/`
- **Business logic?** → `services/`
- **Validation?** → `utils/validators.py`
- **Documentation?** → `docs/`

## 🔄 Data Flow

```
User Interaction
    ↓
ui/ (User Interface)
    ↓
services/ (Business Logic)
    ↓
database/queries/ (SQL Queries)
    ↓
MySQL Database
```

## 📝 File Naming Convention

### Python Files
```
snake_case.py        → All Python files
__init__.py          → Package initializers
```

### Folders
```
lowercase/           → All folders lowercase
queries/             → Plural for collections
auth/                → Singular for modules
```

### Documentation
```
UPPERCASE.md         → Documentation files
README.md            → Main readme
DOCUMENTATION.md     → Complete guide
```

## 🎨 Organization Benefits

### ✅ Clean Root Directory
- Only essential files at root level
- Easy to find main.py and config.py
- No clutter

### ✅ Logical Grouping
- Code organized by layer (database, services, ui)
- Documentation in docs/
- Scripts in scripts/
- Resources in assets/

### ✅ Easy Navigation
- Clear folder names
- Consistent structure
- Predictable locations

### ✅ Scalable
- Easy to add new features
- Clear where new files go
- Maintains organization as project grows

## 📊 File Count by Folder

```
database/            3 files (connection + 2 queries)
services/            2 files (auth + registration)
ui/auth/             2 files (login + register)
utils/               1 file (validators)
docs/                3 files (documentation + SQL)
scripts/             1 file (test script)
Root level/          5 files (main, config, env, requirements, readme)
```

**Total: ~17 files** (clean and manageable!)

## 🚀 Quick Reference

### Starting Development
1. Read `README.md` (5 min)
2. Read `docs/DOCUMENTATION.md` (15 min)
3. Run `scripts/test_dependencies.py`
4. Run `main.py`

### Adding a Feature
1. Create query file in `database/queries/`
2. Create service file in `services/`
3. Create UI file in `ui/`
4. Update `docs/DOCUMENTATION.md` if needed

### Finding Information
- **Quick start** → `README.md`
- **Complete guide** → `docs/DOCUMENTATION.md`
- **Database schema** → `docs/create_database.sql`
- **Code examples** → Look in existing files

## 🎯 Best Practices

### Do's ✅
- Keep root directory clean
- Put documentation in docs/
- Put scripts in scripts/
- Follow the 3-layer pattern
- Use descriptive file names

### Don'ts ❌
- Don't put random files in root
- Don't mix documentation with code
- Don't skip the service layer
- Don't create files without purpose

## 📈 As Project Grows

### Add New Modules
```
database/queries/
  ├── user_queries.py
  ├── registration_queries.py
  ├── immunization_queries.py    ← New
  └── maternal_queries.py         ← New

services/
  ├── auth_service.py
  ├── registration_service.py
  ├── immunization_service.py     ← New
  └── maternal_service.py         ← New

ui/
  ├── auth/
  ├── dashboard/                  ← New
  ├── immunization/               ← New
  └── maternal/                   ← New
```

### Structure Stays Clean
- New features follow same pattern
- Easy to find related files
- Maintains organization
- Scales naturally

---

## 🎉 Result

A **clean, professional, well-organized project** that:

✅ Easy to navigate
✅ Clear structure
✅ Logical grouping
✅ Scalable design
✅ Professional appearance
✅ Team-friendly
✅ Maintainable

**Everything has its place, and every place has its purpose!** 📁
