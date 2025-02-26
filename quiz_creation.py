from db import execute_query


def create_quiz_from_ui(theme, difficulty, question, answer, option_A, option_B, option_C, option_D, points):
    """Create a quiz and insert a question from the UI input."""

    print("Received values:")
    print(f"Theme: {theme}, Difficulty: {difficulty}, Question: {question}")
    print(f"Options: A={option_A}, B={option_B}, C={option_C}, D={option_D}, Answer={answer}, Points={points}")

    if not theme or not question or not option_A or not option_B or not option_C or not option_D or not answer:
        print("Error: Some fields are empty.")
        return "All fields must be filled!"

    # Format table name
    table_name = f"quiz_{theme.replace(' ', '_')}"

    # Create table if it doesn't exist
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS "{table_name}" (
        quiz_id SERIAL PRIMARY KEY,
        theme VARCHAR(255) NOT NULL,
        difficulty INT CHECK (difficulty BETWEEN 1 AND 3) NOT NULL,
        question TEXT NOT NULL,
        answer CHAR(1) NOT NULL,
        option_A TEXT NOT NULL,
        option_B TEXT NOT NULL,
        option_C TEXT NOT NULL,
        option_D TEXT NOT NULL,
        points_value INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    '''
    execute_query(create_table_query)
    print(f"Table '{table_name}' checked or created successfully.")

    # Insert the question into the database
    insert_query = f'''
    INSERT INTO "{table_name}" (theme, difficulty, question, answer, option_A, option_B, option_C, option_D, points_value)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''
    execute_query(insert_query, (theme, difficulty, question, answer, option_A, option_B, option_C, option_D, points))
    print("Question inserted into database.")

    return "Question added successfully!"
