

def main():
    print("===== SAMSON WORKOUT TRACKER =====")
    print("1. Start Session")
    print("2. See Graphs")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        start_session()
    elif choice == "2":
        view_graphs()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
