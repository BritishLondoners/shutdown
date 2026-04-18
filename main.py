def shutdown_program():
    # Ask the user for input
    command = input("Do you want to shutdown the system? (yes/no): ").strip().lower()

    # Decision making
    if command == "yes":
        print("Shutting down...")
        # In a real system, you might call OS commands here
        # Example (Windows): os.system("shutdown /s /t 1")
        # Example (Linux/Mac): os.system("shutdown now")
    elif command == "no":
        print("Shutdown cancelled.")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

# Run the program
shutdown_program()
