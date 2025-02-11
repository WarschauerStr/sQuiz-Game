import psycopg2
from db import execute_query


def create_quiz():
    print("\n📝 Create Your Own Quiz!")

    # Get and validate theme (table name)
    while True:
        theme = input("Enter the quiz theme (e.g., History, Science): ").strip().lower()
        if theme:
            break
        print("⚠ Theme cannot be empty!")

    table_name = f"quiz_{theme.replace(' ', '_')}"  # Format theme for table name

    # Create table if it doesn't exist
    create_table_query = f"""
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
    """
    execute_query(create_table_query)
    print(f"✅ Quiz table '{table_name}' is ready!")

    while True:
        print("\n➕ Add a new question:")

        question = input("Enter the question: ").strip()

        # Get options
        option_A = input("Enter option A: ").strip()
        option_B = input("Enter option B: ").strip()
        option_C = input("Enter option C: ").strip()
        option_D = input("Enter option D: ").strip()

        # Validate answer
        while True:
            answer = input("Enter the correct answer (A, B, C, or D): ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                break
            print("⚠ Invalid answer! Please enter A, B, C, or D.")

        # Validate difficulty level
        while True:
            try:
                difficulty = int(input("Enter difficulty level (1-Easy, 2-Medium, 3-Hard): ").strip())
                if difficulty in [1, 2, 3]:
                    break
            except ValueError:
                pass
            print("⚠ Invalid difficulty! Please enter 1, 2, or 3.")

        # Validate points value
        while True:
            try:
                points = int(input("Enter points value: ").strip())
                if points > 0:
                    break
            except ValueError:
                pass
            print("⚠ Invalid points value! Please enter a positive number.")

        # Insert the question into the database
        insert_query = f"""
        INSERT INTO "{table_name}" (theme, difficulty, question, answer, option_A, option_B, option_C, option_D, points_value)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        execute_query(insert_query, (theme, difficulty, question, answer, option_A, option_B, option_C, option_D, points))
        print("✅ Question added successfully!")

        # Ask if the user wants to add another question
        add_more = input("\nDo you want to add another question? (yes/no): ").strip().lower()
        if add_more != "yes":
            break

    print(f"\n🎉 Quiz '{theme.capitalize()}' created successfully!")
