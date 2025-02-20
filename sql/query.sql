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

-- 1.2.1 Add extension for the password heshing
CREATE EXTENSION IF NOT EXISTS pgcrypto;

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

