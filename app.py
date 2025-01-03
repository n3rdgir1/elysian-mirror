"""
This module contains a Flask web application that uses the Ollama Llama3 model
to generate responses based on user-provided prompts.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_ollama.llms import OllamaLLM
from util.database import initialize_database, get_session, vector_store
from util.models.embeddings import Embedding
from util.models.metadata import Metadata
from llm.embedder import embed
from llm.generate_response import generate_response
from llm.rag import rag

app = Flask(__name__)
CORS(app)  # Enable CORS for the app

# Initialize database
initialize_database()
session = get_session()

# Initialize the LLM with Ollama Llama3
llm = OllamaLLM(model="llama3")

@app.route('/generate', methods=['POST'])
def generate():
    """
    Generate a response using the LLM based on the provided prompt.

    Returns:
        A JSON response containing the generated text.
    """
    data = request.json
    prompt = data.get('prompt', '')

    # Generate a response using the LLM
    response = generate_response(session, prompt)

    return jsonify({'response': response, 'sources': []})

@app.route('/system_prompt', methods=['GET'])
def get_system_prompt():
    """
    Retrieve the system prompt from the database.

    Returns:
        A JSON response containing the system prompt or an error message.
    """
    system_prompt = Metadata().get_system_prompt(session)
    return jsonify({"system_prompt": system_prompt})

@app.route('/system_prompt', methods=['PUT'])
def update_system_prompt():
    """
    Update the system prompt in the database.

    Returns:
        A JSON response indicating success or an error message.
    """
    data = request.json
    description = data.get('description')
    if not description:
        return jsonify({"error": "Description is required"}), 400

    # Update or insert the system prompt
    metadata = Metadata()
    metadata.update_system_prompt(session, description)

    return jsonify({"message": "System prompt updated successfully"})

@app.route('/embed', methods=['POST'])
def embed_text():
    """
    Embed a title and description and save it to the database.

    Returns:
        A JSON response indicating success or an error message.
    """
    data = request.json
    title = data.get('title')
    description = data.get('description')
    if not title or not description:
        return jsonify({"error": "Title and description are required"}), 400

    # Generate embeddings
    embed(title, description)

    return jsonify({"message": "Embedding saved successfully"})

@app.route('/rag', methods=['POST'])
def rag_endpoint():
    """
    Retrieve and generate an answer for a given question using RAG.

    Returns:
        A JSON response containing the generated answer and sources.
    """
    data = request.json
    question = data.get('prompt', '')

    # Retrieve and generate an answer using RAG
    result = rag(question)

    return jsonify({'answer': result['answer'], 'sources': result['sources']})

@app.route('/knowledge', methods=['GET'])
def get_knowledge():
    """
    Retrieve knowledge items from the vector store.

    Returns:
        A JSON response containing a list of knowledge items.
    """
    knowledge_items = []
    for doc in Embedding().all(session):
        title, description = doc.document.split('\n', 1)
        knowledge_items.append({'title': title, 'description': description, 'id': doc.id})

    return jsonify({'knowledge': knowledge_items})

@app.route('/delete_knowledge', methods=['POST'])
def delete_knowledge():
    """
    Delete a knowledge item from the vector store.

    Returns:
        A JSON response indicating success or an error message.
    """
    data = request.json
    knowledge_id = data.get('id')
    if not knowledge_id:
        return jsonify({"error": "Knowledge ID is required"}), 400

    # Delete the knowledge item from the vector store
    vector_store.delete(ids=[knowledge_id])

    return jsonify({"message": "Knowledge item deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
