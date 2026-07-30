import sqlite3

connection = sqlite3.connect("sports.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS AI_Reports (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT,
    report TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()
connection.close()

print("AI_Reports table created successfully!")