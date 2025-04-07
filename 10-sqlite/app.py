import sqlite3
from pathlib import Path

DB_FILE = "sample.sqlite"

def create_connection(db_file):
    """Create a database connection and return the connection object."""
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    """Create a table if it doesn't exist."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    );
    """
    conn.execute(create_table_sql)
    conn.commit()

def insert_user(conn, name, age):
    """Insert a new user into the users table."""
    conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

def get_users(conn):
    """Query all users."""
    cursor = conn.execute("SELECT id, name, age FROM users")
    users = cursor.fetchall()
    return users

def update_user(conn, user_id, new_age):
    """Update a user's age."""
    conn.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
    conn.commit()

def delete_user(conn, user_id):
    """Delete a user by ID."""
    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

def main():
    print("🔧 SQLite CRUD Example")

    # Create database file if not exists
    if not Path(DB_FILE).exists():
        print(f"📁 Creating new database: {DB_FILE}")
    else:
        print(f"📂 Using existing database: {DB_FILE}")

    conn = create_connection(DB_FILE)

    # Create table
    create_table(conn)

    # Insert users
    insert_user(conn, "Alice", 30)
    insert_user(conn, "Bob", 25)

    # Read users
    print("👥 Users after insert:")
    for user in get_users(conn):
        print(user)

    # Update user
    update_user(conn, 1, 31)
    print("🔄 Updated Alice's age:")
    for user in get_users(conn):
        print(user)

    # Delete user
    delete_user(conn, 2)
    print("❌ Deleted Bob:")
    for user in get_users(conn):
        print(user)

    conn.close()
    print("✅ Done.")

if __name__ == "__main__":
    main()
