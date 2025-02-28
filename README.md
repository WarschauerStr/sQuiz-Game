# sQuiz Game

**sQuiz Game** is a fun, interactive quiz application built with Python, PostgreSQL, and PySide2 (Qt for Python). It enables users to register, log in, take quizzes, view leaderboards, and even create custom quizzes. The app features dynamic quiz generation based on themes and difficulty levels, ensuring a unique experience with every playthrough.

## Concept

The core idea of sQuiz Game is to provide an engaging quiz experience where users can:
- **Register and log in** with secure credentials.
- **Select a quiz theme and difficulty level** to tailor the quiz to their interests and challenge.
- **Take quizzes** with randomly selected questions from a PostgreSQL database.
- **View their scores** and compare with others on a leaderboard.
- **Create custom quizzes** by defining new themes, questions, answers, and options—all dynamically stored in the database.

## Features

1. **User Registration and Login**
   - **Registration:** Users sign up by providing their full name, email, username, and password. Passwords are validated to meet security criteria.
   - **Login:** Registered users log in using their username and password. Unique UUIDs ensure user identification remains distinct.

2. **Quiz Participation**
   - **Theme and Difficulty Selection:** Users choose from available quiz themes (e.g., Nature, History, Science) and select a difficulty level (Easy, Medium, or Hard).
   - **Randomized Questions:** Quiz questions are randomly selected from dynamically created tables in the PostgreSQL database.
   - **Scoring:** Points are awarded based on correct answers, and the total score is updated and stored.

3. **Leaderboard**
   - Displays the top players based on their accumulated quiz scores.

4. **Custom Quiz Creation**
   - Users can design their own quizzes by specifying a theme, difficulty, question, possible answers, and the correct answer.
   - The app dynamically creates new quiz tables (e.g., `quiz_nature`, `quiz_science`) to store custom quizzes without altering the core schema.

5. **Asynchronous Operations**
   - **Threading:** Heavy database operations (such as creating tables and inserting questions) are executed on background threads. This prevents the main UI from freezing and ensures smooth user interaction.

## Techniques Used

1. **Dynamic Table Creation:**  
   For custom quizzes, tables are created on-the-fly in PostgreSQL using a naming convention based on the quiz theme. This allows the app to handle new themes without needing to modify the database schema.

2. **Random Question Selection:**  
   Questions for a quiz are fetched randomly from the database, which keeps the quiz experience fresh and challenging on each playthrough.

3. **QStackedWidget for Window Management:**  
   The user interface is built using PySide2. QStackedWidget is used to manage multiple screens (such as login, quiz selection, gameplay, and quiz creation) within a single window, allowing for smooth transitions between different app states.

4. **Asynchronous Database Operations:**  
   To maintain a responsive UI, potentially long-running database queries (such as table creation or question insertion) are offloaded to background threads. This is implemented using Python's threading library.

5. **Input Validation and Security:**  
   - **Regular Expressions (Regex):** Used for validating user inputs such as full names, email addresses, and passwords to ensure data consistency and security.
   - **Password Security:** Passwords are validated to ensure they contain a mix of characters and meet minimum length requirements. They are stored securely using techniques like cryptographic hashing.

6. **UUID for Unique User Identification:**  
   Every registered user is assigned a unique UUID, ensuring that each user is distinctly identified and helping prevent duplicate accounts.

7. **Modular Code Design:**  
   The application is divided into multiple modules:
   - **db.py:** Handles all interactions with the PostgreSQL database.
   - **quiz_creation.py:** Manages custom quiz creation and dynamic table generation.
   - **game_window.py & select_quiz_window.py:** Handle quiz gameplay and quiz selection, respectively.
   - **user.py & validators.py:** Manage user registration, login, and input validation.

## Technologies Used

- **Python:** Core language for implementing the application logic.
- **PostgreSQL:** Database engine for storing user information, quiz questions, and scores.
- **PySide2 (Qt for Python):** Used to build the graphical user interface (GUI) and manage application windows.
- **psycopg2:** Python library for interacting with PostgreSQL.
- **Threading:** Python's built-in threading library is used to execute database operations asynchronously.
- **Regular Expressions (Regex):** Used for input validation to ensure data integrity.

## How to Run the App

1. **Install Dependencies:**  
   Use the command below to install required packages:
   ```bash
   pip install -r requirements.txt
