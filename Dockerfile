FROM python:3.11-slim

WORKDIR /app

# Only copy what is absolutely necessary
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything in the current folder to /app
COPY . .

# Set the environment to show logs immediately
ENV PYTHONUNBUFFERED=1

# Run the main script (Double check if your file is actually named main.py)
CMD ["python", "main.py"]
