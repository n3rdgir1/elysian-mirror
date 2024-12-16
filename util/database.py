import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
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
    Base.metadata.create_all(engine)


def get_session():
    """
    Get a new SQLAlchemy session.

    Returns:
        Session: A new SQLAlchemy session.
    """
    return Session()
