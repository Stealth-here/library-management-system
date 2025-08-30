import sqlite3

def get_connection():
    return sqlite3.connect('library.db')

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   author TEXT NOT NULL,
                   year INTEGER,
                   isbn TEXT UNIQUE)
""")
    conn.commit()
    conn.close()