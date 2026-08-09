"""Password hashing utilities (Task 5). Do not store plain text passwords."""
from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password: str) -> str:
    """Return a secure hash of the password for storage."""
    return generate_password_hash(password, method="scrypt")


def verify_password(password_hash: str, password: str) -> bool:
    """Return True if the given password matches the stored hash."""
    return check_password_hash(password_hash, password)
