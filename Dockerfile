FROM python:3.8-slim

# Write Python output immediately to the STDOUT
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "phlasch/main.py"]
