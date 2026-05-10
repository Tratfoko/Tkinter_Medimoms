"""
User database queries
All SQL operations related to users table
"""

from database.connection import get_connection
from typing import Optional, Dict, List

def get_user_by_username_or_email(username_or_email: str) -> Optional[Dict]:
    """Get user by username or email"""
    conn = get_connection()
    if not conn:
        return None
    
    try:
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
    except Exception as e:
        print(f"[ERROR] Query error: {e}")
        if conn:
            conn.close()
        return None

def update_last_login(user_id: int) -> bool:
    """Update user's last login timestamp"""
    conn = get_connection()
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        query = "UPDATE users SET last_login = NOW() WHERE id = %s"
        cursor.execute(query, (user_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"[ERROR] Update error: {e}")
        if conn:
            conn.close()
        return False

def get_user_barangays(user_id: int) -> List[Dict]:
    """Get barangays assigned to a user"""
    conn = get_connection()
    if not conn:
        return []
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT b.id, b.name
            FROM barangays b
            INNER JOIN user_barangays ub ON b.id = ub.barangay_id
            WHERE ub.user_id = %s
            ORDER BY b.name
        """
        cursor.execute(query, (user_id,))
        barangays = cursor.fetchall()
        cursor.close()
        conn.close()
        return barangays
    except Exception as e:
        print(f"[ERROR] Query error: {e}")
        if conn:
            conn.close()
        return []
