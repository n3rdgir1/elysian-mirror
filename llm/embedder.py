from langchain_core.documents import Document
from util.database import vector_store

def embed(title, description):
    vector_store.add_documents([Document(f"{title}\n{description}")])
