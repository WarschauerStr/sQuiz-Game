import re


def validate_fullname(fullname):
    """Validate the fullname format (e.g. John Smith)."""
    pattern = r"^[A-Za-z]+ [A-Za-z]+$"
    return bool(re.match(pattern, fullname))


def validate_email(email):
    """Validate email format."""
    pattern = r"^\S+@\S+\.\S+$"
    return bool(re.match(pattern, email))


def validate_password(password):
    """Validate password format (at least 8 chars, 1 uppercase, 1 number)."""
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    return bool(re.match(pattern, password))
