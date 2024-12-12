from flask import Flask, request, jsonify
from langchain import LLM

app = Flask(__name__)

# Initialize the LLM with Ollama Llama3
llm = LLM(model_name="ollama-llama3")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')

    # Generate a response using the LLM
    response = llm.generate(prompt)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
