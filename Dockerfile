FROM python:3.11-slim

WORKDIR /app

# Copy everything (main, response, detection, etc.)
COPY . .

# Force terminal output to show up live
ENV PYTHONUNBUFFERED=1

# The ignition switch
CMD ["python", "main.py"]
