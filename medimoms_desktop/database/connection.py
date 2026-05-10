"""
Database connection module for MediMoms Desktop Application
Uses MySQL connection pooling for efficient database operations
"""

import mysql.connector
from mysql.connector import pooling
from config import DB_CONFIG

# Connection pool
connection_pool = None

def init_connection_pool():
    """Initialize MySQL connection pool"""
    global connection_pool
    try:
        connection_pool = pooling.MySQLConnectionPool(
            pool_name="medimoms_pool",
            pool_size=5,
            pool_reset_session=True,
            **DB_CONFIG
        )
        print("[OK] Database connection pool initialized")
        return True
    except mysql.connector.Error as err:
        print(f"[ERROR] Database connection error: {err}")
        return False

def get_connection():
    """Get a connection from the pool"""
    try:
        return connection_pool.get_connection()
    except mysql.connector.Error as err:
        print(f"[ERROR] Error getting connection: {err}")
        return None

def test_connection():
    """Test database connection"""
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            cursor.fetchone()
            cursor.close()
            conn.close()
            return True
        except mysql.connector.Error as err:
            print(f"[ERROR] Connection test failed: {err}")
            return False
    return False
