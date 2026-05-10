"""
Authentication service for user login and session management
"""

import bcrypt
from typing import Tuple, Dict, Optional
from database.queries.user_queries import get_user_by_username_or_email, update_last_login, get_user_barangays
from utils.validators import sanitize_input

def authenticate_user(username_or_email: str, password: str) -> Tuple[bool, Dict | str]:
    """
    Authenticate user with username/email and password
    Returns: (success: bool, user_data: dict or error_message: str)
    """
    # Sanitize input
    username_or_email = sanitize_input(username_or_email)
    
    if not username_or_email or not password:
        return False, "Username and password are required"
    
    # Get user from database
    user = get_user_by_username_or_email(username_or_email)
    
    if not user:
        return False, "Invalid username or password"
    
    # Check account status
    status_messages = {
        'pending': "Your account is pending approval. Please wait for admin approval.",
        'rejected': "Your account has been rejected. Please contact the administrator.",
        'inactive': "Your account has been disabled. Please contact the administrator."
    }
    
    if user['status'] in status_messages:
        return False, status_messages[user['status']]
    
    if user['status'] != 'approved':
        return False, "Invalid account status"
    
    # Verify password
    if not verify_password(password, user['password']):
        return False, "Invalid username or password"
    
    # Update last login
    update_last_login(user['id'])
    
    # Build user session data
    user_data = build_user_session(user)
    
    return True, user_data

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password against bcrypt hash
    Handles both Laravel ($2y$) and Python ($2b$) bcrypt formats
    """
    try:
        # Convert Laravel bcrypt format to Python format
        if hashed_password.startswith('$2y$'):
            hashed_password = '$2b$' + hashed_password[4:]
        
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] Password verification error: {e}")
        return False

def build_user_session(user: Dict) -> Dict:
    """
    Build user session data from database user record
    """
    # Build full name
    full_name = user['first_name']
    if user.get('middle_name'):
        full_name += f" {user['middle_name']}"
    full_name += f" {user['last_name']}"
    
    # Get assigned barangays
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

def hash_password(password: str) -> str:
    """
    Hash password using bcrypt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
