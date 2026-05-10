"""
Registration service for user account creation
"""

from typing import Tuple, Dict
from database.queries.registration_queries import (
    check_username_exists, 
    check_email_exists, 
    create_user,
    get_all_barangays,
    assign_user_barangays
)
from services.auth_service import hash_password
from utils.validators import validate_email, validate_username, validate_password, sanitize_input

def register_midwife(registration_data: Dict) -> Tuple[bool, str]:
    """
    Register a new midwife account
    Returns: (success: bool, message: str)
    """
    
    # Sanitize inputs
    first_name = sanitize_input(registration_data.get('first_name', ''))
    middle_name = sanitize_input(registration_data.get('middle_name', ''))
    last_name = sanitize_input(registration_data.get('last_name', ''))
    username = sanitize_input(registration_data.get('username', ''))
    email = sanitize_input(registration_data.get('email', ''))
    password = registration_data.get('password', '')
    confirm_password = registration_data.get('confirm_password', '')
    contact_number = sanitize_input(registration_data.get('contact_number', ''))
    barangay_ids = registration_data.get('barangay_ids', [])
    
    # Validate required fields
    if not all([first_name, last_name, username, email, password, confirm_password]):
        return False, "All required fields must be filled"
    
    # Validate username
    valid, msg = validate_username(username)
    if not valid:
        return False, msg
    
    # Validate email
    if not validate_email(email):
        return False, "Invalid email format"
    
    # Validate password
    valid, msg = validate_password(password)
    if not valid:
        return False, msg
    
    # Check password match
    if password != confirm_password:
        return False, "Passwords do not match"
    
    # Check if username exists
    if check_username_exists(username):
        return False, "Username already exists"
    
    # Check if email exists
    if check_email_exists(email):
        return False, "Email already exists"
    
    # Validate barangay selection
    if not barangay_ids:
        return False, "Please select at least one barangay"
    
    # Hash password
    hashed_password = hash_password(password)
    
    # Prepare user data
    user_data = {
        'first_name': first_name,
        'middle_name': middle_name if middle_name else None,
        'last_name': last_name,
        'username': username,
        'email': email,
        'password': hashed_password,
        'contact_number': contact_number if contact_number else None,
        'role': 'midwife',
        'status': 'pending'  # Requires admin approval
    }
    
    # Create user
    user_id = create_user(user_data)
    
    if not user_id:
        return False, "Failed to create account. Please try again."
    
    # Assign barangays
    if not assign_user_barangays(user_id, barangay_ids):
        return False, "Account created but failed to assign barangays. Please contact admin."
    
    return True, "Registration successful! Your account is pending admin approval."

def get_barangay_list():
    """Get list of all barangays for selection"""
    return get_all_barangays()
