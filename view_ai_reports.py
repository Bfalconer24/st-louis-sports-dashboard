import sqlite3

connection = sqlite3.connect("sports.db")
cursor = connection.cursor()

cursor.execute("""
SELECT report_id, report_type, subject, created_at
FROM AI_Reports
""")

reports = cursor.fetchall()

for report in reports:
    print(report)

connection.close()