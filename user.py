import uuid
from db import execute_query
from validators import validate_fullname, validate_email, validate_password


def register_user():
    print("Register a new user:")

    # Validate fullname
    while True:
        fullname = input("Enter fullname (First Last): ").strip()
        if validate_fullname(fullname):
            break
        print("⚠ Invalid fullname format. Please use 'First Last'.")

    # Validate email
    while True:
        email = input("Enter email: ").strip()
        if validate_email(email):
            break
        print("⚠ Invalid email format. Please enter a valid email (e.g., user@example.com).")

    # Validate password
    while True:
        password = input("Enter password (min 8 chars, 1 uppercase, 1 number): ").strip()
        if validate_password(password):
            break
        print("⚠ Invalid password. It must be at least 8 characters long, contain at least one uppercase letter and one number.")

    # Get username (no strict validation, but ensure it's not empty)
    while True:
        username = input("Enter username: ").strip()
        if username:
            break
        print("⚠ Username cannot be empty.")

    user_uuid = str(uuid.uuid4())

    insert_query = """
    INSERT INTO users (uuid, fullname, email, password, username)
    VALUES (%s, %s, %s, crypt(%s, gen_salt('md5')), %s);
    """
    execute_query(insert_query, (user_uuid, fullname, email, password, username))
    print("✅ Registration successful!")


def login_user():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    select_query = """
    SELECT * FROM users
    WHERE username = %s AND password = crypt(%s, password);
    """
    user = execute_query(select_query, (username, password), fetch=True)

    if user:
        print(f"Welcome, {user[0][2]}!")  # Display fullname
        return user[0]  # Return user details as a tuple
    else:
        print("Invalid username or password.")
        return None


def update_user_score(user_id, score):
    check_query = "SELECT points FROM score WHERE user_id = %s;"
    existing_score = execute_query(check_query, (user_id,), fetch=True)

    if existing_score:
        new_score = existing_score[0][0] + score
        update_query = "UPDATE score SET points = %s WHERE user_id = %s;"
        execute_query(update_query, (new_score, user_id))
    else:
        insert_query = "INSERT INTO score (user_id, points) VALUES (%s, %s);"
        execute_query(insert_query, (user_id, score))

    print(f"Your total score is now {new_score if existing_score else score} points!")
