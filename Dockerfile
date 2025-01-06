# Use a multi-stage build to build the frontend and backend

# Stage 1: Build the frontend
FROM node:14 AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Build the backend
FROM python:3.8-slim AS backend-builder
WORKDIR /app
# Install libpq-dev for psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Copy the built frontend files to the backend container
COPY --from=frontend-builder /app/frontend/dist /app/frontend/dist

# Expose port 5000 for the Flask application
EXPOSE 5000

# Set the entrypoint to run the Flask application
ENTRYPOINT ["python", "app.py"]
