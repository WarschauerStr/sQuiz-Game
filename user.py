import uuid
from db import execute_query
from validators import validate_fullname, validate_email, validate_password


def register_user(fullname, email, password, username):
    """Register a new user with provided details."""
    if not validate_fullname(fullname):
        print("⚠ Invalid fullname format. Please use 'First Last'.")
        return
    
    if not validate_email(email):
        print("⚠ Invalid email format. Please enter a valid email (e.g., user@example.com).")
        return

    if not validate_password(password):
        print("⚠ Invalid password. It must be at least 8 characters long, contain at least one uppercase letter and one number.")
        return
    
    user_uuid = str(uuid.uuid4())

    insert_query = """
    INSERT INTO users (uuid, fullname, email, password, username)
    VALUES (%s, %s, %s, crypt(%s, gen_salt('md5')), %s);
    """
    execute_query(insert_query, (user_uuid, fullname, email, password, username))
    print("✅ Registration successful!")


def login_user(username, password):
    """Login user and return user details if successful."""
    select_query = """
    SELECT * FROM users
    WHERE username = %s AND password = crypt(%s, password);
    """
    user = execute_query(select_query, (username, password), fetch=True)

    if user:
        return user[0]  # Return user details as a tuple
    else:
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
