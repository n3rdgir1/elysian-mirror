# Flask Application with pgvector

This project is a Flask web application that uses `pgvector` for vector storage and retrieval, along with `langchain` for language model interactions.

## Prerequisites

- Docker
- Python 3.8+
- pip

## Setup Instructions

### Step 1: Run pgvector in a Docker Container

1. Pull the Docker image for PostgreSQL with pgvector:

   ```bash
   docker pull ankane/pgvector
   ```

2. Run the Docker container:

   ```bash
   docker run --name pgvector -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 ankane/pgvector
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

1. Update the `DATABASE_URL` in `util/database.py` with your database connection string. For example:

   ```python
   DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"
   ```

### Step 4: Run the Application

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Access the application at `http://localhost:5000`.

## Endpoints

- `POST /generate`: Generate a response using the LLM based on the provided prompt.
- `GET /system_prompt`: Retrieve the current system prompt.
- `PUT /system_prompt`: Update the system prompt.
