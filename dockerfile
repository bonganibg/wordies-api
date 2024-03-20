# Use a slim Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy your FastAPI application code
COPY . .

# Run the application using Gunicorn with Uvicorn
CMD ["Uvicorn", "main:app", "--host", "0.0.0.0"]