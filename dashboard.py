import sqlite3
import pandas as pd

print("=" * 50)
print("     ST. LOUIS SPORTS INSIGHT DASHBOARD")
print("=" * 50)

connection = sqlite3.connect("sports.db")

players = pd.read_sql_query("""
SELECT player_name, position, nationality
FROM Players
""", connection)

connection.close()

# Summary statistics
total_players = len(players)
unique_positions = players["position"].nunique()
unique_nationalities = players["nationality"].nunique()

print("\nChoose an option:")
print("1. View Summary")
print("2. View Top Positions")
print("3. Exit")

choice = input("\nSelection: ")

if choice == "1":
    print(f"\nTotal Players: {total_players}")
    print(f"Unique Positions: {unique_positions}")
    print(f"Unique Nationalities: {unique_nationalities}")

elif choice == "2":
    print("\n=== Top Positions ===")
    for position, count in position_counts.items():
        print(f"{position}: {count}")

elif choice == "3":
    print("\nGoodbye!")

else:
    print("\nInvalid selection.")