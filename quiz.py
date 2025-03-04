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

