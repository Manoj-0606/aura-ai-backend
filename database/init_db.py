# database/init_db.py

import sqlite3

conn = sqlite3.connect("database/memory.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_profile (
    id INTEGER PRIMARY KEY,
    name TEXT,
    weight REAL,
    goal TEXT,
    diet TEXT
)
""")

cursor.execute("""
INSERT OR REPLACE INTO user_profile
(id, name, weight, goal, diet)
VALUES
(1, 'Manoj', 85, 'Lose 10kg', 'Vegetarian')
""")

conn.commit()
conn.close()

print("Database Created")