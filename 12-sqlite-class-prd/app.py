import sqlite3
import logging
from typing import Any, List, Optional, Tuple, Union

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class SQLiteDB:
    def __init__(self, db_path: str, row_as_dict: bool = False):
        """
        Initialize the SQLiteDB wrapper.

        :param db_path: Path to the SQLite database file.
        :param row_as_dict: If True, fetches rows as dictionaries.
        """
        self.db_path = db_path
        self.row_as_dict = row_as_dict
        self.conn = sqlite3.connect(db_path, timeout=30)
        if row_as_dict:
            self.conn.row_factory = sqlite3.Row

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def execute(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> None:
        """Execute a write query (INSERT/UPDATE/DELETE)."""
        try:
            with self.conn:
                self.conn.execute(query, params or ())
        except sqlite3.Error as e:
            logger.exception(f"SQLite execute error: {e}")
            raise

    def executemany(self, query: str, data: List[Tuple[Any, ...]]) -> None:
        """Execute a batch write query."""
        try:
            with self.conn:
                self.conn.executemany(query, data)
        except sqlite3.Error as e:
            logger.exception(f"SQLite executemany error: {e}")
            raise

    def fetchall(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> List[Union[Tuple, dict]]:
        """Fetch all results from a SELECT query."""
        try:
            cursor = self.conn.execute(query, params or ())
            return cursor.fetchall()
        except sqlite3.Error as e:
            logger.exception(f"SQLite fetchall error: {e}")
            raise

    def fetchone(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> Optional[Union[Tuple, dict]]:
        """Fetch the first result from a SELECT query."""
        try:
            cursor = self.conn.execute(query, params or ())
            return cursor.fetchone()
        except sqlite3.Error as e:
            logger.exception(f"SQLite fetchone error: {e}")
            raise

    def create_table(self, create_sql: str) -> None:
        """Create a table from a SQL string."""
        try:
            with self.conn:
                self.conn.execute(create_sql)
        except sqlite3.Error as e:
            logger.exception(f"SQLite create_table error: {e}")
            raise

    def close(self) -> None:
        """Close the connection."""
        if self.conn:
            self.conn.close()
            logger.info("SQLite connection closed.")

def main():
    with SQLiteDB("sample.sqlite", row_as_dict=True) as db:
        db.create_table("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        """)

        db.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
        db.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
            ("Bob", 25),
            ("Charlie", 40)
        ])

        users = db.fetchall("SELECT * FROM users")
        for user in users:
            print(dict(user))  # Easy column access if row_as_dict=True

if __name__ == "__main__":
    main()
