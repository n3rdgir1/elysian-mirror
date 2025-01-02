"Base RAG implementation to use as a baseline"

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM

from util.database import vector_store

RAG_PROMPT = PromptTemplate(
    input_variables=["question", "context"],
    template="""You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise.

Question: {question}

Context: {context}

Answer:"""
)

def retrieve(question: str):
    """Retrieve documents for a given question."""
    docs = vector_store.as_retriever().invoke(question, top_k=5)
    sources = []
    for doc in docs:
        title, description = doc.page_content.split('\n', 1)
        sources.append({'title': title, 'description': description})
    return docs, sources

def answer_with_context(question: str, docs: str):
    """Utilizes a LLM to answer the question with a given context.

    Args:
        question (str): The question to answer.
        docs (str): The context to use for answering the question.

    Returns:
        str: The answer to the question.
    """
    llm = OllamaLLM(model="llama3")

    generation = RAG_PROMPT | llm | StrOutputParser()

    return generation.invoke({"context": docs, "question": question})

def rag(question: str):
    """Retrieve and generate an answer for a given question using RAG.

    Args:
        question (str): The question to answer.

    Returns:
        dict: The answer to the question and the sources.
    """

    docs, sources = retrieve(question)
    answer = answer_with_context(question, docs)
    return {'answer': answer, 'sources': sources}
