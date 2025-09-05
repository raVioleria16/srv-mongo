FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir -r requirements.txt

# Copia TUTTO il contenuto nella cartella /app
COPY app/* .

CMD ["python", "app.py"]
