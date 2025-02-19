import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from langchain_postgres import PGVector
from langchain_ollama.embeddings import OllamaEmbeddings

Base = declarative_base()
ollama_url = os.getenv('OLLAMA_URL', 'http://localhost:11434')
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://mirror:mysecretpassword@localhost:6024/mirror")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
vector_store = PGVector(
    embeddings=OllamaEmbeddings(model="phi3:mini", base_url=ollama_url),
    collection_name='embeddings',
    connection=DATABASE_URL,
    use_jsonb=True,
)

def initialize_database():
    """
    Initialize the database by creating the necessary tables if they do not exist.
    """
    # Create table if not exists
    vector_store.create_collection()
    Base.metadata.create_all(engine)


def get_session():
    """
    Get a new SQLAlchemy session.

    Returns:
        Session: A new SQLAlchemy session.
    """
    return Session()
