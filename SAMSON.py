# SAMSON Workout Tracker for TI-84 Plus CE Python
# File-I/O-free version using ti_system variable storage
# Includes pre-defined workout data and skippable timer

import time
from datetime import datetime

# Try to import ti_system (only exists on TI-84)
try:
    import ti_system  # type: ignore
except ImportError:
    # Mock version for desktop testing
    class ti_system:
        _storage = {}
        @staticmethod
        def setVar(name, value):
            ti_system._storage[name] = value
        @staticmethod
        def getVar(name):
            return ti_system._storage.get(name, "No data saved.")


DEFAULT_REST = 3  # minutes

# ==========================================
# 🏋️‍♂️ PRE-DEFINED WORKOUT DATA
# ==========================================
WORKOUT_PLAN = {
    "Abs": [("+1", "Crunch")],
    "Triceps": [
        ("+1", "Supinated Push Down"),
        ("-2", "Overhead Press (Descending)"),
        ("-3", "Overhead Press (Ascending)"),
        ("-4", "Shoulder Extension (90–0)")
    ],
    "Back": [
        ("+1", "Sagittal Row"),
        ("+2", "Frontal Plane Pulldown"),
        ("+3", "Kelso Row")
    ],
    "Quads": [("+1", "Leg Extension")],
    "Hamstrings": [
        ("+1", "Seated Curl"),
        ("-2", "Lying Curl"),
        ("-3", "45° Curl")
    ],
    "Chest": [
        ("+1", "Machine Chest Press"),
        ("-2", "Upper"),
        ("-3", "Lower")
    ],
    "Biceps": [
        ("+1", "Recline Curl"),
        ("-2", "30° Curl"),
        ("-3", "Supinations")
    ],
    "Shoulders": [
        ("+1", "Lateral Raise"),
        ("-2", "Rear"),
        ("-3", "Front Delt")
    ],
    "Forearms": [
        ("-1", "Pronated Curl"),
        ("+2", "Supinated Curl")
    ],
    "Calves": [
        ("+1", "Toes In"),
        ("+2", "Toes Out"),
        ("+3", "Seated")
    ],
    "Glutes": [("+1", "Thrust")]
}

# Filter only "+" exercises for the active session
ACTIVE_WORKOUTS = {
    group: [name for code, name in exs if code.startswith("+")]
    for group, exs in WORKOUT_PLAN.items()
    if any(code.startswith("+") for code, _ in exs)
}


# ==========================================
# ⏱️ TIMER WITH MID-SKIP SUPPORT
# ==========================================

def start_timer(rest_time=DEFAULT_REST):
    """Countdown rest timer in minutes with skip option."""
    print(f"Rest for {rest_time} minutes. (Press Enter to skip)\n")
    total = rest_time * 60

    try:
        import sys, select  # Only works on desktop, not TI-84
        for remaining in range(total, 0, -1):
            mins, secs = divmod(remaining, 60)
            time_format = f"{mins:02d}:{secs:02d}"
            print(f"\rRest time left: {time_format}", end="")
            time.sleep(1)

            # Check for Enter press
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                sys.stdin.readline()  # Clear input
                print("\nTimer skipped!\n")
                return
        print("\nRest over!\n")

    except Exception:
        # TI-84 fallback: no select module
        for remaining in range(total, 0, -1):
            mins, secs = divmod(remaining, 60)
            print(f"\rRest time left: {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
        print("\nRest over!\n")


# ==========================================
# 💾 STORAGE + SESSION LOGIC
# ==========================================
def read_last_workout():
    """Displays the last saved workout."""
    try:
        print("=== LAST RECORDED WORKOUT ===")
        print(ti_system.getVar("LASTWORK"))
    except Exception:
        print("No previous workout found.\n")


def save_last_workout(entries):
    """Saves workout summary into TI variable storage."""
    summary_lines = [f"Session Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}"]
    for exercise, reps, weight in entries:
        summary_lines.append(f"{exercise}: {reps} reps @ {weight} lbs")
    ti_system.setVar("LASTWORK", "\n".join(summary_lines))
    print("\nWorkout saved!\n")


def start_session():
    """Runs a workout session using the active exercises."""
    print("=== SAMSON WORKOUT SESSION ===")
    read_last_workout()
    entries = []

    # Show workout layout
    print("Today's Active Exercises:")
    for group, exs in ACTIVE_WORKOUTS.items():
        print(f"\n[{group}]")
        for ex in exs:
            print(f"  - {ex}")
    print()

    # Logging section
    for group, exs in ACTIVE_WORKOUTS.items():
        print(f"\n--- {group.upper()} ---")
        for exercise in exs:
            print(f"\nExercise: {exercise}")
            reps = input("  Reps: ").strip()
            weight = input("  Weight (lbs): ").strip()
            entries.append((exercise, reps, weight))

            skip = input("  Start rest timer? (y/n): ").strip().lower()
            if skip == "y":
                start_timer(DEFAULT_REST)
            else:
                print("  Skipping rest timer...")

    if entries:
        save_last_workout(entries)
    else:
        print("No exercises recorded.\n")


# ==========================================
# 🧭 MAIN MENU
# ==========================================
def main():
    print("=== SAMSON ===")
    print("1. Start Session")
    print("2. View Last Workout")
    choice = input("Select an option (1/2): ").strip()

    if choice == "1":
        start_session()
    elif choice == "2":
        read_last_workout()
    else:
        print("Invalid choice.\n")


if __name__ == "__main__":
    main()
