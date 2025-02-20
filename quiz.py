from db import execute_query
from user import update_user_score


def get_available_themes():
    query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_name LIKE 'quiz_%';
    """
    tables = execute_query(query, fetch=True)

    themes = set()
    for table in tables:
        table_name = table[0]
        theme_query = f"SELECT DISTINCT theme FROM \"{table_name}\";"
        table_themes = execute_query(theme_query, fetch=True)
        for theme in table_themes:
            themes.add(theme[0].lower())

    return sorted(themes)


def get_quiz_questions(theme, difficulty):
    table_name = f"quiz_{theme.replace(' ', '_').lower()}"
    query = f"""
    SELECT quiz_id, question, answer, option_A, option_B, option_C, option_D,
    points_value
    FROM \"{table_name}\"
    WHERE LOWER(theme) = %s AND difficulty = %s
    ORDER BY RANDOM()
    LIMIT 10;
    """
    questions = execute_query(query, (theme.lower(), difficulty), fetch=True)
    return questions


def start_quiz_menu(user_id):
    themes = get_available_themes()
    if themes:
        print("\n\U0001F4DA Available themes:")
        for theme in themes:
            print(f"\u2705 {theme.capitalize()}")
        theme = input("\n\U0001F3AD Choose a theme: ").strip().lower()
        if theme in themes:
            difficulty = input("Choose difficulty level (1-Easy, 2-Medium, 3-Hard): ").strip()
            questions = get_quiz_questions(theme, difficulty)
            if questions:
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
                print(f"You finished the quiz with {score} points!")
                update_user_score(user_id, score)  # Update score after quiz
            else:
                print("No questions available for this theme and difficulty.")
        else:
            print("Invalid theme. Please try again.")
    else:
        print("No themes available.")
