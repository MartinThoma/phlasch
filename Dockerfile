# Phlasch Server Docker image
# This is a multi-stage Dockerfile which helps us separate the build
# from release and not include the OS packages needed to install the
# requirements. (We can't delete them cause Dockerfile layers are read only)

# ---------------------------------------------------------------- build stage

FROM python:3.8-alpine AS builder

WORKDIR /app

RUN apk add --no-cache build-base postgresql-dev

RUN python -m venv venv

RUN venv/bin/pip install --upgrade pip setuptools

COPY requirements.txt .

RUN venv/bin/pip install --trusted-host pypi.python.org \
                         --no-cache-dir \
                         -r requirements.txt

# -------------------------------------------------------------- release stage

FROM python:3.8-alpine

WORKDIR /app

COPY --from=builder /app .

COPY . .

ENV PATH="/app/venv/bin:$PATH"

# Write Python output immediately to the STDOUT
ENV PYTHONUNBUFFERED 1

# Don't create .pyc files in the Docker container
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8080

CMD ["python", "phlasch/main.py"]
