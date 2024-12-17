from sqlalchemy import Column, String, Text
from util.database import Base

class Embedding(Base):
    """
    view embedded document sources.
    """
    __tablename__ = 'langchain_pg_embedding'
    id = Column(String, primary_key=True)
    document = Column(Text)

    def all(self, session):
        """
        Retrieve all embedded documents from the database.

        Args:
            session: A SQLAlchemy session.

        Returns:
            list: All embedded documents.
        """
        return session.query(Embedding).all()
