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

# Expose port (adjust if needed)
EXPOSE 8000

# Run the application using Gunicorn with Uvicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]