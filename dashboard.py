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


position_counts = players["position"].value_counts()
running = True

while running:


    print("\nChoose an option:")
    print("1. View Summary")
    print("2. View Top Positions")
    print("3. View AI Scout Reports")
    print("4. Exit")

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

            connection = sqlite3.connect("sports.db")

            reports = pd.read_sql_query("""
            SELECT subject, report_type
            FROM AI_Reports
            """, connection)

            connection.close()

            print("\n=== AI Scout Reports ===")

            for index, row in reports.iterrows():
                print("-" * 40)
                print(f"Subject : {row['subject']}")
                print(f"Type    : {row['report_type']}")

    elif choice == "4":
            print("\nGoodbye!")
            running = False

    else:
            print("\nInvalid selection.") 