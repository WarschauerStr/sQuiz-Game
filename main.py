from user import register_user, login_user
from quiz import start_quiz_menu
from leaderboard import get_top_users
from quiz_creation import create_quiz


def show_main_menu():
    print("=" * 40)
    print("\U0001F389 Welcome to the sQuiz Game! \U0001F389".center(40))
    print("=" * 40)
    print("\n\U0001F3C1 Main Menu:")
    print("1️⃣ Register")
    print("2️⃣ Login")
    print("3️⃣ Exit")


def show_user_options():
    print("\n\U0001F3AF Welcome back!")
    print("1️⃣ Start Quiz")
    print("2️⃣ View Leaderboard")
    print("3️⃣ Create a Quiz")
    print("4️⃣ Log Out")


def main():
    while True:
        show_main_menu()
        action = input("\n\U0001F449 Choose an option (1-3): ").strip()

        if action == "1":  # Register
            register_user()
            if input("Would you like to login now? (yes/no): ").strip().lower() == "yes":
                user = login_user()
                if user:
                    user_id = user[0]
                    print("\n\U0001F3AF Login successful!")
                    while True:
                        show_user_options()
                        option = input("\nChoose an option (1-4): ").strip()
                        if option == "1":
                            start_quiz_menu(user_id)
                        elif option == "2":
                            get_top_users()
                        elif option == "3":
                            create_quiz()
                        elif option == "4":
                            print("\n\U0001F44B Goodbye! See you next time!")
                            break
                        else:
                            print("⚠ Invalid choice. Please choose between 1-4.")
                else:
                    print("\nLogin failed!")
        elif action == "2":  # Login
            user = login_user()
            if user:
                user_id = user[0]
                print("\n\U0001F3AF Login successful!")
                while True:
                    show_user_options()
                    option = input("\nChoose an option (1-4): ").strip()
                    if option == "1":
                        start_quiz_menu(user_id)
                    elif option == "2":
                        get_top_users()
                    elif option == "3":
                        create_quiz()
                    elif option == "4":
                        print("\n\U0001F44B Goodbye! See you next time!")
                        break
                    else:
                        print("⚠ Invalid choice. Please choose between 1-4.")
            else:
                print("Invalid username or password.")
        elif action == "3":  # Exit
            print("\n\U0001F44B Goodbye! See you next time!")
            break
        else:
            print("⚠ Invalid choice. Please choose between 1-3.")


if __name__ == "__main__":
    main()
