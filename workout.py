# Workout Tracker for TI-84 Plus CE Python
# Author: Minhhai Quach
# Platform: TI-84 Plus CE Python
# Description: Simple workout logging and viewing app

from ti_system import *
from ti_draw import *
from ti_image import *
from ti_math import *

# -------------------------
# Data storage (persistent)
# -------------------------
# L1: Exercise name (string)
# L2: Sets
# L3: Reps
# L4: Weight

def init_lists():
    try:
        L1
    except:
        store_list([], "L1")
        store_list([], "L2")
        store_list([], "L3")
        store_list([], "L4")

# -------------------------
# Utility
# -------------------------
def pause():
    input("Press ENTER")

def clear():
    cls()

# -------------------------
# Add workout
# -------------------------
def add_workout():
    clear()
    print("ADD WORKOUT")

    name = input("Exercise: ")
    sets = int(input("Sets: "))
    reps = int(input("Reps: "))
    weight = int(input("Weight: "))

    L1.append(name)
    L2.append(sets)
    L3.append(reps)
    L4.append(weight)

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
        print("   Sets:", L2[i])
        print("   Reps:", L3[i])
        print("   Wt  :", L4[i])
        print("")

    pause()

# -------------------------
# Clear workouts
# -------------------------
def clear_workouts():
    clear()
    confirm = input("Clear all? (y/n): ")
    if confirm == "y":
        L1.clear()
        L2.clear()
        L3.clear()
        L4.clear()
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
        print("3. Clear workouts")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            add_workout()
        elif choice == "2":
            view_workouts()
        elif choice == "3":
            clear_workouts()
        elif choice == "4":
            clear()
            break

# -------------------------
# Program start
# -------------------------
init_lists()
main_menu()
