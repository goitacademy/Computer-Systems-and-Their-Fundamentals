import sqlite3
from contextlib import contextmanager

database = "./test.db"


@contextmanager
def create_connection(db_file):
    """create a database connection to a SQLite database"""
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()
