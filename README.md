# Flask Application with pgvector

This project is a Flask web application that uses `pgvector` for vector storage and retrieval, along with `langchain` for language model interactions.

## Prerequisites

- Docker
- Python 3.8+
- pip
- ollama

## Setup Instructions

### Step 1: Run pgvector in a Docker Container

1. Pull the Docker image for PostgreSQL with pgvector:

   ```bash
   docker pull ankane/pgvector
   ```

2. Run the Docker container:

   ```bash
   docker run --name pgvector -e POSTGRES_USER=mirror -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=mirror -d -p 6024:5432 pgvector/pgvector:pg16
   ```

   Replace `mysecretpassword` with a secure password of your choice.

### Step 2: Install Python Dependencies

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Configure the Database

1. Set the `DATABASE_URL` environment variable with your database connection string. For example:

   ```bash
   export DATABASE_URL="postgresql://mirror:mysecretpassword@localhost:6024/mirror"
   ```

### Step 4: Build the UI

1. Navigate to the `frontend` directory:

   ```bash
   cd frontend
   ```

2. Install the frontend dependencies:

   ```bash
   npm install
   ```

3. Build the UI:

   ```bash
   npm run build
   ```

### Step 5: Run the Application

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Access the application at `http://localhost:5000`.

### Step 6: Install Ollama models

1. Install the necessary models

   ```bash
   ollama pull phi3:mini
   ollama pull mistral
   ```

### Running the API in Development Mode

To run the API in development mode, set the `FLASK_DEBUG` environment variable to `True`:

```bash
export FLASK_DEBUG=True
```

Then start the Flask application as usual:

```bash
python app.py
```

## Endpoints

- `POST /generate`: Generate a response using the LLM based on the provided prompt. The response includes the generated text and an optional array of sources.
- `GET /system_prompt`: Retrieve the current system prompt.
- `PUT /system_prompt`: Update the system prompt.
- `POST /embed`: Embed a title and description and save it to the database.
- `POST /rag`: Retrieve and generate an answer for a given question using RAG. The response includes the generated answer and an array of sources.
