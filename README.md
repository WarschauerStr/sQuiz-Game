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
   - **Threading:** Heavy database operations (such as creating tables and inserting questions) can be executed on background threads. This prevents the main UI from freezing and ensures smooth user interaction.

6. **Input Validation and Security**
   - **Regular Expressions (Regex):** Used for validating user inputs such as full names, email addresses, and passwords to ensure data consistency and security.
   - **Password Security:** Passwords are validated to ensure they contain a mix of characters and meet minimum length requirements. They are stored securely using techniques like cryptographic hashing.

## Techniques Used

1. **Dynamic Table Creation:**  
   For custom quizzes, tables are created on-the-fly in PostgreSQL using a naming convention based on the quiz theme. This allows the app to handle new themes without needing to modify the database schema.

2. **Random Question Selection:**  
   Questions for a quiz are fetched randomly from the database, which keeps the quiz experience fresh and challenging on each playthrough.

3. **QStackedWidget for Window Management:**  
   The user interface is built using PySide2. QStackedWidget is used to manage multiple screens (such as login, quiz selection, gameplay, and quiz creation) within a single window, allowing for smooth transitions between different app states.

4. **Asynchronous Database Operations:**  
   To maintain a responsive UI, potentially long-running database queries (such as table creation or question insertion) can be offloaded to background threads. This is implemented using Python's threading library.

5. **UUID for Unique User Identification:**  
   Every registered user is assigned a unique UUID, ensuring that each user is distinctly identified and helping prevent duplicate accounts.

## 7. Modular Code Design

The application is organized into multiple files and directories, each serving a distinct purpose. Below is an overview of the primary files and their responsibilities:

- **`main.py`**  
  The entry point of the application. Initializes the PySide2 application, sets up the `QStackedWidget`, and manages transitions between different windows. Also stores the current user's ID.

- **`db.py`**  
  Handles all interactions with the PostgreSQL database. Exposes functions to connect, execute queries, and fetch results.

- **`quiz_creation.py`**  
  Manages the creation of custom quizzes. Dynamically generates new quiz tables (e.g., `quiz_nature`, `quiz_science`) and inserts user-defined questions into the database.

- **`quiz.py`**  
  Contains functions for retrieving quiz questions from the database (e.g., `get_quiz_questions`) and managing quiz data outside the user interface.

- **`leaderboard.py`**  
  Provides functionality to query the database for top user scores, enabling the leaderboard feature.

- **`user.py`**  
  Handles user-related operations such as registration, login, and updating user scores.

- **`validators.py`**  
  Contains regular expressions and helper methods for validating user inputs like full names, emails, and passwords.

- **`requirements.txt`**  
  Lists all Python dependencies (e.g., `PySide2`, `psycopg2`, etc.) required to run the application.

### The `windows` Directory

Inside the `windows` folder, each Python file corresponds to a specific GUI window. These files load `.ui` files created in Qt Designer and handle window-specific logic:

- **`login_register_window.py`**  
  Displays the login and register interface, allowing users to sign in or create a new account.

- **`register_window.py`**  
  A separate window (if you prefer a dedicated registration screen) for collecting user registration details.

- **`logged_options_window.py`**  
  Shown after a user logs in, presenting options like “Start Quiz,” “Create Quiz,” “View Leaderboard,” or “Log Out.”

- **`select_quiz_window.py`**  
  Allows users to choose a quiz theme and difficulty before starting the quiz. Validates the user’s selection and only creates a `GameWindow` if there are valid questions.

- **`game_window.py`**  
  Displays the quiz questions, handles user answers, and updates the user’s score. It fetches or receives a list of quiz questions and manages the quiz flow (showing the next question, finishing the quiz, etc.).

- **`create_quiz_window.py`**  
  Provides a form for users to input new quiz data (theme, difficulty, question, answers). Sends this data to `quiz_creation.py` to dynamically create or update quiz tables.

### The `ui` Directory

Holds `.ui` files designed in Qt Designer. Each `.ui` file corresponds to a window or dialog in the application (e.g., `login_register_window.ui`, `select_quiz_window.ui`). PySide2’s `QUiLoader` is used to load these interfaces into the corresponding Python classes.

---

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
