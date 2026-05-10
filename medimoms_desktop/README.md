# MediMoms Desktop Application

Modern healthcare management system for midwives in Santa Cruz, Laguna.

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure database (edit config.py or .env)
DB_NAME=medimoms_system
DB_USER=root
DB_PASSWORD=your_password

# Run application
python main.py
```

## 📁 Project Structure

```
medimoms_desktop/
├── 📂 database/            # Database layer (SQL queries)
│   ├── connection.py      # MySQL connection pool
│   └── queries/           # Query modules
│
├── 📂 services/           # Business logic layer
│   ├── auth_service.py
│   └── registration_service.py
│
├── 📂 ui/                 # User interface layer
│   ├── auth/              # Authentication screens
│   └── components/        # Reusable UI components
│
├── 📂 utils/              # Utilities (validation, helpers)
│
├── 📂 docs/               # Documentation & SQL files
│   ├── DOCUMENTATION.md   # Complete guide
│   └── create_database.sql
│
├── 📂 scripts/            # Utility scripts
│   └── test_dependencies.py
│
├── 📂 assets/             # Images, icons, resources
│
├── 📄 main.py             # Application entry point
├── 📄 config.py           # Configuration
├── 📄 .env                # Environment variables
├── 📄 requirements.txt    # Dependencies
└── 📄 README.md           # This file
```

## ✨ Features

- ✅ **Login System** - Secure authentication with bcrypt
- ✅ **Registration** - Self-service midwife registration
- ✅ **Modern UI** - Professional emerald green theme
- ✅ **Secure** - SQL injection prevention, password hashing
- ✅ **Clean Code** - MVC architecture, type hints

## 📚 Documentation

See **[docs/DOCUMENTATION.md](docs/DOCUMENTATION.md)** for:
- Complete architecture guide
- Design system reference
- How to add new features
- Database schema
- Troubleshooting

## 🔐 Security

- Bcrypt password hashing
- Parameterized SQL queries
- Input sanitization
- Connection pooling
- Account status validation

## 🛠️ Tech Stack

- **UI**: CustomTkinter
- **Database**: MySQL (mysql-connector-python)
- **Security**: bcrypt
- **Validation**: pydantic
- **Language**: Python 3.8+

## 📝 Development

### Architecture
```
UI Layer → Service Layer → Database Layer → MySQL
```

### Adding Features
1. Create queries in `database/queries/`
2. Create service in `services/`
3. Create UI in `ui/`
4. Follow design system (see DOCUMENTATION.md)

## 🎨 Design System

- **Colors**: Emerald green (#10B981) theme
- **Font**: Segoe UI
- **Style**: Modern, clean, professional
- **Layout**: Centered cards, generous spacing

## 🧪 Testing

```bash
# Test dependencies
python scripts/test_dependencies.py

# Test database connection
python main.py
```

## 📞 Support

For issues or questions, check **docs/DOCUMENTATION.md** for:
- Troubleshooting guide
- Common issues
- Development workflow
- Best practices

---

**Built with ❤️ for healthcare workers in Santa Cruz, Laguna**
