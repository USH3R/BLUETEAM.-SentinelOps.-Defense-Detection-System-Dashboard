FROM python:3.11-slim
WORKDIR /app
COPY settings.yaml .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py ingestion.py detection.py response.py reporting.py ./
COPY auth.log .
RUN mkdir -p /app/logs && chmod 777 /app/logs
VOLUME ["/app/logs"]
CMD ["python", "main.py"]
