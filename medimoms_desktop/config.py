# Configuration file for MediMoms Desktop Application

import os
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
if env_path.exists():
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value

# Database Configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'database': os.getenv('DB_NAME', 'medimoms_system'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', '4110')
}

# Application Configuration
APP_NAME = os.getenv('APP_NAME', 'MediMoms')
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')

# UI Theme Colors (matching web app design)
COLORS = {
    'background': '#ECFDF5',  # Light emerald background
    'sidebar': '#10B981',  # Emerald green
    'accent': '#10B981',  # Emerald green
    'success': '#10B981',  # Emerald green
    'warning': '#F59E0B',
    'danger': '#EF4444',
    'card': '#ffffff',
    'text': '#0F172A',  # Slate 900
    'text_secondary': '#64748B'  # Slate 500
}

# Window Configuration
WINDOW_SIZE = "1200x700"
MIN_WINDOW_SIZE = (1000, 600)
