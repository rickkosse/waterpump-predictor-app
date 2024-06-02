# Gebruik een officiële Python runtime als een parent image
FROM python:3.11-slim

# Zet de werkdirectory in de container
WORKDIR /app

# Kopieer de requirements file in de container
COPY requirements.txt /app/

# Installeer de Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer de rest van de applicatie code in de container
COPY . /app

# Specificeer de command om je app te runnen
CMD ["python", "app.py"]

# Exposeer de juiste poort
EXPOSE 5000
