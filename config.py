"""
Application configuration.
Loads environment variables and defines base Flask settings.
"""
import os
from dotenv import load_dotenv

load_dotenv()


def _get_database_url():
    """Build SQLAlchemy DATABASE_URL from env. Prefer DATABASE_URL if set."""
    url = os.environ.get("DATABASE_URL")
    if url:
        return url
    host = os.environ.get("MYSQL_HOST") or os.environ.get("DB_HOST") or "localhost"
    port = os.environ.get("MYSQL_PORT") or os.environ.get("DB_PORT") or "3306"
    user = os.environ.get("MYSQL_USER") or os.environ.get("DB_USER") or "root"
    password = os.environ.get("MYSQL_PASSWORD") or os.environ.get("DB_PASSWORD") or "2004"
    dbname = os.environ.get("MYSQL_DATABASE") or os.environ.get("DB_NAME") or "ConnectX"
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"


class Config:
    """Base configuration."""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-key-change-in-production"
    DEBUG = os.environ.get("DEBUG", "false").lower() in ("true", "1", "yes")

    # Database (MySQL via SQLAlchemy)
    SQLALCHEMY_DATABASE_URI = _get_database_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Profile image upload (Task 9)
    UPLOAD_FOLDER = "static/uploads/profiles"
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
