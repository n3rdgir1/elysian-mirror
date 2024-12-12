import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://mirror:mysecretpassword@localhost:6024/mirror")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def initialize_database():
    """
    Initialize the database by creating the necessary tables if they do not exist.
    """
    # Create table if not exists
    with engine.connect() as connection:
        connection.execute(text("""
        CREATE TABLE IF NOT EXISTS metadata (
            name TEXT PRIMARY KEY,
            description TEXT
        )
        """))

def get_session():
    """
    Get a new SQLAlchemy session.

    Returns:
        Session: A new SQLAlchemy session.
    """
    return Session()
