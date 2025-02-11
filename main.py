from user import register_user, login_user, update_user_score
from quiz import get_available_themes, get_quiz_questions
from quiz_creation import create_quiz


def display_quiz(theme, user_id):
    while True:
        difficulty = input("Choose difficulty level (1-Easy, 2-Medium, 3-Hard): ").strip()
        if difficulty in ["1", "2", "3"]:
            difficulty = int(difficulty)
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    questions = get_quiz_questions(theme, difficulty)

    if not questions:
        print("No questions available for this theme and difficulty.")
        return

    score = 0
    for idx, (quiz_id, question, answer, option_A, option_B, option_C, option_D, points) in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {question}")
        print(f"A. {option_A}\nB. {option_B}\nC. {option_C}\nD. {option_D}")

        user_answer = input("Your answer (A, B, C, D): ").strip().upper()

        if user_answer == answer:
            print("Correct!\n")
            score += points
        else:
            print(f"Wrong! The correct answer was {answer}.\n")

    update_user_score(user_id, score)
    print(f"You finished the quiz with {score} points!\n")


def start_quiz(user_id):
    themes = get_available_themes()

    if themes:
        print("\n\U0001F4DA Available themes:")
        for theme in themes:
            print(f"\u2705 {theme.capitalize()}")

        while True:
            selected_theme = input("\n\U0001F3AD Choose a theme: ").strip().lower()

            if selected_theme in themes:
                display_quiz(selected_theme, user_id)
                break
            else:
                print("\u26A0 Invalid theme. Please select from the available themes.")
    else:
        print("\u26A0 No themes available in the database.")


def main():
    print("=" * 40)
    print("\U0001F389 Welcome to the sQuiz Game! \U0001F389".center(40))
    print("=" * 40)

    while True:
        print("\n\U0001F3C1 Main Menu:")
        print("1️⃣ Register")
        print("2️⃣ Login")
        print("3️⃣ Create a Quiz")
        print("4️⃣ Exit")

        action = input("\n\U0001F449 Choose an option (1-4): ").strip()

        if action == "1":  # Register
            register_user()

        elif action == "2":  # Login
            while True:
                user = login_user()

                if user:
                    user_id = user[0]
                    print("\n\U0001F3AF Login successful!")
                    print(f"\U0001F44B Welcome, {user[2]}!\n")
                    start_quiz(user_id)
                    break
                else:
                    retry = input("\n\U0001F504 Login failed. Try again? (yes/no): ").strip().lower()
                    if retry != "yes":
                        break

        elif action == "3":  # Create a Quiz
            create_quiz()

        elif action == "4":  # Exit
            print("\n\U0001F44B Thanks for playing sQuiz Game! See you next time! \U0001F680")
            break

        else:
            print("⚠ Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
