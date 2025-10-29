import time
from datetime import datetime

DATABASE_FILE = "DATABASE.txt"
DEFAULT_REST = 3  # minutes


def read_database():
    """Reads previous workout records from DATABASE.txt"""
    try:
        with open(DATABASE_FILE, "r") as file:
            data = file.readlines()
            print("=== Last Recorded Workouts ===")
            for line in data[-5:]:  # show last 5 entries
                print(line.strip())
    except FileNotFoundError:
        print("No previous database found. Starting fresh.")
    print()


def start_timer(rest_time=DEFAULT_REST):
    """Rest timer in minutes"""
    print(f"Rest for {rest_time} minutes.")
    for remaining in range(rest_time * 60, 0, -1):
        mins, secs = divmod(remaining, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(f"\rRest time left: {time_format}", end="")
        time.sleep(1)
    print("\nRest over!\n")


def write_to_database(entries):
    """Writes completed session to DATABASE.txt"""
    with open(DATABASE_FILE, "a") as file:
        file.write(f"\nSession Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for exercise, reps, weight in entries:
            file.write(f"{exercise}: {reps} reps @ {weight} lbs\n")
    print("Workout saved to database.\n")


def start_session():
    """Runs a workout session"""
    print("=== SAMSON WORKOUT SESSION ===")
    read_database()
    entries = []

    while True:
        exercise = input("Enter exercise name (or 'done' to finish): ").strip()
        if exercise.lower() == "done":
            break

        reps = input("Enter number of reps: ").strip()
        weight = input("Enter weight (lbs): ").strip()

        entries.append((exercise, reps, weight))
        start_timer(DEFAULT_REST)

    if entries:
        write_to_database(entries)
    else:
        print("No exercises recorded.")


def main():
    print("=== SAMSON ===")
    print("1. Start Session")
    print("2. Read Database")
    choice = input("Select an option (1/2): ").strip()

    if choice == "1":
        start_session()
    elif choice == "2":
        read_database()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
