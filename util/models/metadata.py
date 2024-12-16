"metadata"
from sqlalchemy import Column, Text, String
from util.database import Base

class Metadata(Base):
    """
    Metadata table for storing metadata about the app.
    """
    __tablename__ = 'metadata'
    name = Column(String, primary_key=True)
    description = Column(Text)

    def get_system_prompt(self, session):
        """
        Retrieve the system prompt from the database.

        Args:
            session: A SQLAlchemy session.

        Returns:
            str: The system prompt.
        """
        result = session.query(Metadata).filter_by(name='system_prompt').first()
        if result:
            return result.description
        return ''

    def update_system_prompt(self, session, description):
        """
        Update the system prompt in the database.

        Args:
            session: A SQLAlchemy session.
            description: The new system prompt.
        """
        result = session.query(Metadata).filter_by(name='system_prompt').first()
        if result:
            result.description = description
        else:
            result = Metadata(name='system_prompt', description=description)
            session.add(result)
        session.commit()
        return result
