# Workout Tracker for TI-84 Plus CE Python
# Author: Minhhai Quach
# Features: Calorie tracking, progressive overload, TI Connect export

from ti_system import *

# -------------------------
# Init persistent lists
# -------------------------
def init_lists():
    for name in ["L1","L2","L3","L4","L5","L6"]:
        try:
            eval(name)
        except:
            store_list([], name)

def clear():
    cls()

def pause():
    input("Press ENTER")

# -------------------------
# Calculations
# -------------------------
def calc_1rm(weight, reps):
    # Epley formula
    return int(weight * (1 + reps / 30))

# -------------------------
# Add workout
# -------------------------
def add_workout():
    clear()
    print("ADD WORKOUT\n")

    name = input("Exercise: ")
    sets = int(input("Sets: "))
    reps = int(input("Reps: "))
    weight = int(input("Weight: "))
    calories = int(input("Calories: "))

    one_rm = calc_1rm(weight, reps)

    L1.append(name)
    L2.append(sets)
    L3.append(reps)
    L4.append(weight)
    L5.append(calories)
    L6.append(one_rm)

    print("\nSaved.")
    pause()

# -------------------------
# View workouts
# -------------------------
def view_workouts():
    clear()
    print("WORKOUT LOG\n")

    if len(L1) == 0:
        print("No workouts saved.")
        pause()
        return

    for i in range(len(L1)):
        print(i + 1, ")", L1[i])
        print(" Sets:", L2[i])
        print(" Reps:", L3[i])
        print(" Wt  :", L4[i])
        print(" Cal :", L5[i])
        print(" 1RM :", L6[i])
        print("")

    pause()

# -------------------------
# Progressive overload check
# -------------------------
def overload_check():
    clear()
    print("PROGRESSIVE OVERLOAD\n")

    if len(L1) < 2:
        print("Not enough data.")
        pause()
        return

    last = len(L1) - 1
    prev = last - 1

    if L6[last] > L6[prev]:
        print("Improvement detected")
        print("+", L6[last] - L6[prev], "1RM")
    elif L6[last] < L6[prev]:
        print("Performance decreased")
    else:
        print("No change")

    pause()

# -------------------------
# Export instructions
# -------------------------
def export_data():
    clear()
    print("EXPORT DATA\n")
    print("1. Connect calculator")
    print("2. Open TI Connect CE")
    print("3. Copy lists:")
    print("   L1–L6")
    print("\nLists can be")
    print("exported as CSV.")
    pause()

# -------------------------
# Clear data
# -------------------------
def clear_workouts():
    clear()
    if input("Clear all? (y/n): ") == "y":
        for lst in [L1,L2,L3,L4,L5,L6]:
            lst.clear()
        print("Cleared.")
    else:
        print("Canceled.")
    pause()

# -------------------------
# Main menu
# -------------------------
def main_menu():
    while True:
        clear()
        print("WORKOUT TRACKER\n")
        print("1. Add workout")
        print("2. View workouts")
        print("3. Overload check")
        print("4. Export data")
        print("5. Clear workouts")
        print("6. Exit")

        c = input("> ")

        if c == "1":
            add_workout()
        elif c == "2":
            view_workouts()
        elif c == "3":
            overload_check()
        elif c == "4":
            export_data()
        elif c == "5":
            clear_workouts()
        elif c == "6":
            break

# -------------------------
# Start
# -------------------------
init_lists()
main_menu()
