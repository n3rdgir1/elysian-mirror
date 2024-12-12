"""
This module contains a Flask web application that uses the Ollama Llama3 model
to generate responses based on user-provided prompts.
"""

from flask import Flask, request, jsonify
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

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
    template = ChatPromptTemplate.from_template("{question}")
    chain = template | llm
    response = chain.invoke({"question": prompt})

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
