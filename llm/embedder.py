"Handle embeddings"

import uuid
from langchain_core.documents import Document
from util.database import vector_store

def embed(title, description):
    """
    Embed a document with the given title and description into the vector store.

    Args:
        title (str): The title of the document.
        description (str): The description of the document.
    """
    doc_id = str(uuid.uuid4())
    metadata = {"title": title, "id": doc_id}
    vector_store.add_documents([Document(page_content=f"{title}\n{description}", metadata=metadata)])

def remove(knowledge_id):
    """
    Remove a document from the vector store using its knowledge ID.

    Args:
        knowledge_id (str): The ID of the document to be removed.
    """
    vector_store.delete(ids=[knowledge_id])
