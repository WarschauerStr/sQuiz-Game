# sQuiz Game

Welcome to **sQuiz Game**! This is a fun and interactive quiz game built using Python, PostgreSQL, and a simple user interface. It allows users to register, login, participate in quizzes, view leaderboards, and even create their own custom quizzes.

## Features

### 1. **User Registration and Login**
- **Registration**: Users can register by providing their **fullname**, **email**, **password**, and **username**.
- **Login**: Registered users can log in using their **username** and **password**.
- **Password Validation**: Passwords are validated to ensure they meet security standards, including a minimum length and a mix of uppercase letters and numbers.

### 2. **Quiz Participation**
- **Quiz Themes**: Users can choose from different quiz themes (e.g., Nature, History, Science).
- **Difficulty Levels**: The game supports three difficulty levels: Easy (1), Medium (2), and Hard (3).
- **Scoring**: Each question has a score associated with it, and users accumulate points based on their correct answers.
- **Random Question Selection**: Questions are selected randomly from the database to provide a unique experience each time.

### 3. **Leaderboard**
- Users can view the leaderboard, which displays the top scorers in the game.

### 4. **Custom Quiz Creation**
- Users can create their own quiz by specifying the **theme**, **difficulty**, **questions**, **answers**, and **options**. The created quiz is then stored in the database.

### 5. **Score Update**
- After completing a quiz, users' scores are updated and stored in the database, allowing them to track their progress over time.

### 6. **Explanation of Techniques**
Explanation of Techniques
1. UUID for User Identification
A unique UUID is generated for each user during registration. This ensures that users are identified uniquely across the system.
2. Password Security
The password validation ensures that passwords meet certain security standards, such as a minimum length and the inclusion of at least one uppercase letter and one number. This is important for preventing weak passwords.
3. Dynamic Quiz Tables
The quiz tables are created dynamically for each theme (e.g., quiz_nature, quiz_science). This approach allows for easy addition of new themes and quizzes without altering the database schema.
4. Random Question Selection
To ensure the game remains fun and challenging, quiz questions are selected randomly from the database for each quiz attempt.
5. Leaderboard
The leaderboard displays the top users based on their accumulated scores, allowing players to see how they rank against others.
6. Database Interaction
The psycopg2 library is used to interact with the PostgreSQL database, execute queries, and fetch results. It provides a simple interface for working with PostgreSQL from Python.

## Technologies Used

### 1. **Python**
- Python is used as the main programming language to implement the game logic.
- The `psycopg2` library is used for interacting with the PostgreSQL database.

### 2. **PostgreSQL**
- A PostgreSQL database is used to store user information, quiz data, and scores.
- The database schema includes tables for users (`users`), quiz scores (`score`), and dynamic quiz tables for different themes.

### 3. **Regular Expressions (Regex)**
- Regex is used for validating user input, such as **fullnames**, **emails**, and **passwords**. This ensures that user data is correctly formatted.

## Database Schema

### `users` Table
Stores information about users, including their **fullname**, **email**, **password**, and **username**.

```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE,
    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
