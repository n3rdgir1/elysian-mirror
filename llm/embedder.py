from langchain_ollama.embeddings import OllamaEmbedder

class Embedder:
    def __init__(self):
        self.embedder = OllamaEmbedder(model="nomic-embed-text")

    def embed(self, text):
        return self.embedder.embed(text)
