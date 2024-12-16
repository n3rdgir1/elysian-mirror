"""
This module contains a Flask web application that uses the Ollama Llama3 model
to generate responses based on user-provided prompts.
"""

from flask import Flask, request, jsonify
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from util.database import initialize_database, get_session
from util.models.metadata import Metadata

app = Flask(__name__)

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
    system_prompt = Metadata().get_system_prompt(session)
    template = ChatPromptTemplate.from_template("{system_prompt}\n{question}")
    chain = template | llm
    response = chain.invoke({"question": prompt, "system_prompt": system_prompt})

    return jsonify({'response': response})

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

if __name__ == '__main__':
    app.run(debug=True)
