from langchain_core.documents import Document
from util.database import vector_store
import uuid

def embed(title, description):
    doc_id = str(uuid.uuid4())
    metadata = {"title": title, "id": doc_id}
    vector_store.add_documents([Document(page_content=f"{title}\n{description}", metadata=metadata)])
