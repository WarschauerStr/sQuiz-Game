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

```sql
-- 1.1 Create database
CREATE DATABASE sQuiz_game;

-- Switch to the created database
\c sQuiz_game;

-- 1.2 Create 'users' table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,    -- Internal auto-increment ID
    uuid UUID NOT NULL UNIQUE,     -- UUID as the primary key
    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,  -- Ensure unique email
    password VARCHAR(255) NOT NULL,     -- Store hashed password here
    username VARCHAR(255) NOT NULL UNIQUE, -- Ensure unique username
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 1.3 Create 'score' table
CREATE TABLE score (
    score_id SERIAL PRIMARY KEY,   -- Primary key for score table
    user_id INT NOT NULL,          -- Foreign key to users table
    points INT NOT NULL,           -- Points scored in the quiz
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- 2.1 Create 'quiz' table
CREATE TABLE quiz_name (
    quiz_id SERIAL PRIMARY KEY,    -- primary key for quiz table
    theme VARCHAR(255) NOT NULL,    -- theme of the quiz
    difficulty INT CHECK (difficulty BETWEEN 1 AND 3) NOT NULL,  -- difficulty level (1-3)
    question TEXT NOT NULL,         -- the quiz question
    answer CHAR(1) NOT NULL,        -- correct answer (A, B, C, D)
    option_A TEXT NOT NULL,         -- option A
    option_B TEXT NOT NULL,         -- option B
    option_C TEXT NOT NULL,         -- option C
    option_D TEXT NOT NULL,         -- option D
    points_value INT NOT NULL,      -- points for this question
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2.2 Add to 'quiz' table
INSERT INTO quiz_name (theme, difficulty, question, answer, option_A, option_B, option_C, option_D, points_value)
VALUES
('Nature', 1, 'What is the largest mammal on Earth?', 'A', 'Blue Whale', 'Elephant', 'Giraffe', 'Shark', 10),
('Nature', 1, 'Which part of the plant conducts photosynthesis?', 'B', 'Roots', 'Leaves', 'Stem', 'Flowers', 10),
('Nature', 1, 'What gas do plants absorb from the atmosphere?', 'C', 'Oxygen', 'Nitrogen', 'Carbon Dioxide', 'Hydrogen', 10),
('Nature', 1, 'What is the fastest land animal?', 'A', 'Cheetah', 'Lion', 'Horse', 'Kangaroo', 10),
('Nature', 1, 'How many legs does a spider have?', 'D', '4', '6', '10', '8', 10),
('Nature', 1, 'Which of these is NOT a type of bear?', 'B', 'Grizzly', 'Panda', 'Polar', 'Tiger', 10),
('Nature', 1, 'What do bees collect from flowers?', 'D', 'Leaves', 'Water', 'Seeds', 'Nectar', 10),
('Nature', 1, 'Which season comes after summer?', 'C', 'Winter', 'Spring', 'Autumn', 'Monsoon', 10),
('Nature', 1, 'Which ocean is the largest?', 'A', 'Pacific', 'Atlantic', 'Indian', 'Arctic', 10),
('Nature', 1, 'What type of animal is a frog?', 'B', 'Reptile', 'Amphibian', 'Mammal', 'Fish', 10);
