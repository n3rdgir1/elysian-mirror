from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "your_database_url_here"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def initialize_database():
    # Create table if not exists
    with engine.connect() as connection:
        connection.execute(text("""
        CREATE TABLE IF NOT EXISTS metadata (
            name TEXT PRIMARY KEY,
            description TEXT,
            embedding VECTOR(1536)
        )
        """))

def get_session():
    return Session()
