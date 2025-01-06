import os
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from util.models.metadata import Metadata


def generate_response(session, prompt):
    """
    Generate a response using the LLM based on the provided prompt.

    Args:
        session: Database session.
        prompt: User-provided prompt.

    Returns:
        The generated response text.
    """
    ollama_url = os.getenv('OLLAMA_URL', 'http://localhost:11434')
    llm = OllamaLLM(model="mistral", base_url=ollama_url)
    system_prompt = Metadata().get_system_prompt(session)
    template = ChatPromptTemplate.from_template("{system_prompt}\n{question}")
    chain = template | llm
    response = chain.invoke({"question": prompt, "system_prompt": system_prompt})
    return response
