1. Registration and login

1.1 User should be able to register new account with:
"fullname, email, password, username",
after that we should generate and attach uuid to the account.

1.2 Login will use username and password to let the user enter account.



2. Creating database and tables

2.1 Create database named "sQuiz_game"

2.2 Create table named "users" for users information: (fullname, email, password, username, etc...).
Use uuid as the primary key instead of user_id. This way, we can maintain uniqueness across multiple systems and avoid relying on sequential integers. We can still have user_id as an auto-increment integer for internal database management.
Example:
"user_id"	"uuid"	"fullname"	"email"	"password"	"username"
1	"b9a1f2e9-8a8a-42e2-8b08-62e5f1a3b9d3"	"Jake Smith"	"jake.smith@example.com"	"password"	"jakesmith"

2.3 Create "score" table. "score" table should contain: (score_id, user_id, points) columns. After completing a quiz points should 
be added to the points column. "user_id" should be automatically added from users table and added to the "score" table.
score_id should be the primary key for the score table, and user_id should be a foreign key referencing the users table. 
Example:
"score_id   "user_id"  "points"
1 "1"    "10"



3. Create "quiz" table.

3.1 "quiz" table should contain: (quiz_id, theme, question, answer, option_A,	option_B,	option_C,	option_D,	points_value)
Example:
"quiz_id"   "theme" "question"  "answer"	"option_A"	"option_B"	"option_C"	"option_D"	"points_value"
1	"Nature"	"What is the largest mammal on Earth?"	"A"	"Blue Whale"	"Elephant"	"Giraffe"	"Shark"	10

4. Main menu structure:

First page:
1. Register
2. Login
3. Exit

Second page:
1. If the user chose registration, execute registration procedure, then ask him
if he would like to login
2. If the user chose login, execute login procedure
3. Exit

Third page:
After user successfully logged in:
1. Option to display available quizes and chose one if he agree,
if not return
2. Display leaderboard
3. Option to create own quiz
4. Exit


ADD LATER:

1. Regex validators for email, password and username.
Email and username should be unique.
Hash passwords
-- CREATE EXTENSION IF NOT EXISTS pgcrypto;

2. After completing a quiz, user will recieve points for it, but should not
be able to recieve points for the same quiz twice next time.
(Later we will create table for users attempts and will compare results from
the previous one and compare with the current one and add the difference to the score table points column. Make sure 
that we don't have to decriese points value.)

3. Create personal cabinet.
Let user display his points.

4. Add leaderboard
