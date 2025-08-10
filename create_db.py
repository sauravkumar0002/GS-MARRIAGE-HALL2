import sqlite3

conn = sqlite3.connect('bookings.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    date TEXT,
    hall_type TEXT,
    status TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
''')

conn.commit()
conn.close()
print("Database and tables created.")
