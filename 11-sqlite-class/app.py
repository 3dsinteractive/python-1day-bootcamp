import sqlite3
from typing import Any, List, Tuple, Optional


class SQLiteDB:
    def __init__(self, db_path: str):
        """
        Initialize the SQLiteDB wrapper.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def execute(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> None:
        """Execute a single query with optional parameters."""
        self.cursor.execute(query, params or ())
        self.conn.commit()

    def executemany(self, query: str, data: List[Tuple[Any, ...]]) -> None:
        """Execute a query for many sets of parameters."""
        self.cursor.executemany(query, data)
        self.conn.commit()

    def fetchall(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> List[Tuple]:
        """Run a SELECT query and return all results."""
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetchone(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> Tuple:
        """Run a SELECT query and return the first result."""
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def create_table(self, create_sql: str) -> None:
        """Create a table using a SQL statement."""
        self.cursor.execute(create_sql)
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        self.conn.close()

def main():
    db = SQLiteDB("sample.sqlite")

    # Create table
    db.create_table("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        );
    """)

    # Insert data
    db.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
    db.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
        ("Bob", 25),
        ("Charlie", 35)
    ])

    # Fetch and print users
    users = db.fetchall("SELECT * FROM users")
    for user in users:
        print(user)

    # Update
    db.execute("UPDATE users SET age = ? WHERE name = ?", (32, "Alice"))

    # Delete
    db.execute("DELETE FROM users WHERE name = ?", ("Bob",))

    db.close()


if __name__ == "__main__":
    main()
