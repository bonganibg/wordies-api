FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN uvicorn main:app --host 0.0.0.0 --port $PORT


