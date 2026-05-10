"""
Registration database queries
All SQL operations related to user registration
"""

from database.connection import get_connection
from typing import Optional, Dict

def check_username_exists(username: str) -> bool:
    """Check if username already exists"""
    conn = get_connection()
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return count > 0
    except Exception as e:
        print(f"[ERROR] Query error: {e}")
        if conn:
            conn.close()
        return False

def check_email_exists(email: str) -> bool:
    """Check if email already exists"""
    conn = get_connection()
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return count > 0
    except Exception as e:
        print(f"[ERROR] Query error: {e}")
        if conn:
            conn.close()
        return False

def create_user(user_data: Dict) -> Optional[int]:
    """Create a new user account"""
    conn = get_connection()
    if not conn:
        return None
    
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO users 
            (first_name, middle_name, last_name, username, email, password, 
             contact_number, role, status, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
        """
        cursor.execute(query, (
            user_data['first_name'],
            user_data.get('middle_name'),
            user_data['last_name'],
            user_data['username'],
            user_data['email'],
            user_data['password'],
            user_data.get('contact_number'),
            user_data.get('role', 'midwife'),
            user_data.get('status', 'pending')
        ))
        conn.commit()
        user_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return user_id
    except Exception as e:
        print(f"[ERROR] Insert error: {e}")
        if conn:
            conn.rollback()
            conn.close()
        return None

def get_all_barangays():
    """Get all barangays for selection"""
    conn = get_connection()
    if not conn:
        return []
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT id, name FROM barangays ORDER BY name"
        cursor.execute(query)
        barangays = cursor.fetchall()
        cursor.close()
        conn.close()
        return barangays
    except Exception as e:
        print(f"[ERROR] Query error: {e}")
        if conn:
            conn.close()
        return []

def assign_user_barangays(user_id: int, barangay_ids: list) -> bool:
    """Assign barangays to a user"""
    conn = get_connection()
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO user_barangays (user_id, barangay_id) VALUES (%s, %s)"
        for barangay_id in barangay_ids:
            cursor.execute(query, (user_id, barangay_id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"[ERROR] Insert error: {e}")
        if conn:
            conn.rollback()
            conn.close()
        return False
