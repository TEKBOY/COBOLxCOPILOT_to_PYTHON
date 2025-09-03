print(">>> main.py is running")   # debug au lancement
from operations import Operations

def main():
    ops = Operations()
    continue_flag = 'YES'
    while continue_flag == 'YES':
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")
        try:
            user_choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input, please enter a number between 1 and 4.")
            continue

        if user_choice == 1:
            ops.process('TOTAL')
        elif user_choice == 2:
            ops.process('CREDIT')
        elif user_choice == 3:
            ops.process('DEBIT')
        elif user_choice == 4:
            continue_flag = 'NO'
        else:
            print("Invalid choice, please select 1-4.")

    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()
