import subprocess
import sys


def run_script(script_name):
    print(f"\nRunning {script_name}...")

    subprocess.run(
        [sys.executable, script_name],
        check=True
    )

    print(f"{script_name} completed successfully.")


def main():
    run_script("database_teams.py")
    run_script("database_players.py")
    run_script("database_events.py")
    run_script("analytics.py")

    print("\nDashboard data update completed successfully.")


if __name__ == "__main__":
    main()