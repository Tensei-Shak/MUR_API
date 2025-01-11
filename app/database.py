import sqlite3 as db

DB_NAME = 'APIESP32.db'

def create_table():
    conn = db.connect(database=DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data_moviments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id TEXT NOT NULL,
            time REAL NOT NULL,
            displacement REAL NOT NULL,
            velocity REAL NOT NULL,
            acceleration REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()
