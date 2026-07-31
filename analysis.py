import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
connection = sqlite3.connect("sports.db")

players = pd.read_sql_query("""
SELECT player_name, position
FROM Players
""", connection)

connection.close()

# Count players by position
position_counts = players["position"].value_counts()

print(position_counts)

# Create chart
plt.figure(figsize=(10,6))

position_counts.plot(kind="bar")

plt.title("Arsenal Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")

plt.tight_layout()

# Create images folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Save chart
plt.savefig("images/players_by_position.png", dpi=300)

print("Chart saved to images/players_by_position.png")

plt.show()