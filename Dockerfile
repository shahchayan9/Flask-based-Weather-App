FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

# CMD ["pytest", "tests"]

EXPOSE 5000

CMD ["python3", "app.py"]
