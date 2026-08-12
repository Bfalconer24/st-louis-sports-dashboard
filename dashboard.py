import sqlite3
import pandas as pd

def load_players():
    connection = sqlite3.connect("sports.db")

    players = pd.read_sql_query("""
        SELECT player_name, position, nationality
        FROM Players
    """, connection)

    connection.close()

    return players

def show_summary(players):
    total_players = len(players)
    unique_positions = players["position"].nunique()
    unique_nationalities = players["nationality"].nunique()

    print(f"\nTotal Players: {total_players}")
    print(f"Unique Positions: {unique_positions}")
    print(f"Unique Nationalities: {unique_nationalities}")

def show_top_positions(players):
    print("\n=== Top Positions ===")


    for position, count in position_counts.items():
        print(f"{position}: {count}")

def show_players_by_nationality(players):
    print("\n=== Players by Nationality ===")

    nationality_counts = players["nationality"].value_counts()

    for nationality, count in nationality_counts.items():
        print(f"{nationality}: {count}")   

 def show_ai_reports():
    connection = sqlite3.connect("sports.db")

    reports = pd.read_sql_query("""
        SELECT report_id, subject, report_type, created_at
        FROM AI_Reports
    """, connection)

    connection.close()

    print("\n=== AI Scout Reports ===")

    for index, row in reports.iterrows():
        created = row["created_at"] if row["created_at"] else "Unknown"

        print("=" * 40)
        print(f"AI SCOUT REPORT #{row['report_id']}")
        print("=" * 40)
        print(f"Subject : {row['subject']}")
        print(f"Type    : {row['report_type']}")
        print(f"Created : {created}")
        print()

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

def main():
    players = load_players()
    running = True

    while running:


        print("\nChoose an option:")
        print("1. View Summary")
        print("2. View Top Positions")
        print("3. View Players by Nationality")
        print("4. View AI Scout Reports")
        print("5. Exit")

        choice = input("\nSelection: ")

        if choice == "1":
            show_summary(players)

        elif choice == "2":
            show_top_positions(players)

        elif choice == "3":
            show_players_by_nationality(players)


        elif choice == "4":
            show_ai_reports()
            

            reports = pd.read_sql_query("""
                SELECT report_id, subject, report_type, created_at
                FROM AI_Reports
            """, connection)

            connection.close()

            print("\n=== AI Scout Reports ===")

            for index, row in reports.iterrows():
                
                created = row["created_at"] if row["created_at"] else "Unknown"

                print("=" * 40)
                print(f"AI SCOUT REPORT #{row['report_id']}")
                print("=" * 40)
                print(f"Subject : {row['subject']}")
                print(f"Type    : {row['report_type']}")
                print(f"Created : {created}")

                print()

        elif choice == "5":
            print("\nGoodbye!")
            running = False
        else:
            print("\nInvalid selection.")
