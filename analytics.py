import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DATABASE_NAME = "sports.db"
ASSETS_DIR = "assets"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def load_players():
    connection = get_connection()

    players = pd.read_sql_query("""
        SELECT player_name, position, nationality
        FROM Players
    """, connection)

    connection.close()

    return players


def create_position_chart(players):
    position_counts = players["position"].value_counts()

    fig, ax = plt.subplots(figsize=(10, 6))

    position_counts.sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_title("Players by Position")
    ax.set_xlabel("Number of Players")
    ax.set_ylabel("Position")

    fig.tight_layout()

    fig.savefig(
        os.path.join(ASSETS_DIR, "position_distribution.png"),
        dpi=200,
        bbox_inches="tight"
    )

    


def create_nationality_chart(players):
    nationality_counts = players["nationality"].value_counts()

    fig, ax = plt.subplots(figsize=(10, 6))

    nationality_counts.sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_title("Players by Nationality")
    ax.set_xlabel("Number of Players")
    ax.set_ylabel("Nationality")

    fig.tight_layout()

    fig.savefig(
        os.path.join(ASSETS_DIR, "nationality_distribution.png"),
        dpi=200,
        bbox_inches="tight"
)
  



def create_events_by_league_chart():
    connection = get_connection()

    events = pd.read_sql_query("""
        SELECT league
        FROM Events
    """, connection)

    connection.close()

    league_counts = events["league"].value_counts()

    fig, ax = plt.subplots(figsize=(10, 6))

    league_counts.sort_values().plot(
        kind="barh",
        ax=ax
    )
    ax.set_xticks(
        range(0, int(league_counts.max()) + 2)
    )

    ax.set_title("Events by League")
    ax.set_xlabel("Number of Events")
    ax.set_ylabel("League")

    fig.tight_layout()

    fig.savefig(
        os.path.join(ASSETS_DIR, "events_by_league.png"),
        dpi=200,
        bbox_inches="tight"
)
    

    


def create_events_over_time_chart():
    connection = get_connection()

    events = pd.read_sql_query("""
        SELECT event_date
        FROM Events
        WHERE event_date IS NOT NULL
    """, connection)

    connection.close()

    events["event_date"] = pd.to_datetime(
        events["event_date"],
        errors="coerce"
    )

    events = events.dropna(subset=["event_date"])

    monthly_events = (
        events
        .set_index("event_date")
        .resample("ME")
        .size()
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    monthly_events.plot(
        kind="line",
        marker="o",
        ax=ax
    )

    if len(monthly_events) == 1:
        ax.set_xlim(
            monthly_events.index[0] - pd.Timedelta(days=15),
            monthly_events.index[0] + pd.Timedelta(days=15)
        )

    ax.set_title("Sports Events Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Events")

    fig.tight_layout()

    fig.savefig(
        os.path.join(ASSETS_DIR, "events_over_time.png"),
        dpi=200,
        bbox_inches="tight"
    )

    
    

def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    players = load_players()

    create_position_chart(players)
    create_nationality_chart(players)
    create_events_by_league_chart()
    create_events_over_time_chart()



if __name__ == "__main__":
    main()