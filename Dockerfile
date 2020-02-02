# Phlasch Docker image
# This is a multi-stage Dockerfile which helps us separate the build
# from release and not include the OS packages needed to install the
# requirements. (We can't delete them cause Dockerfile layers are read only)

# ---------------------------------------------------------------- build stage

# build image
FROM python:3.8-alpine AS builder

# set build working directory
WORKDIR /app

# install build dependencies
RUN apk add --no-cache build-base postgresql-dev libffi-dev

# built packages to be copied over
RUN python -m venv venv

# update pip
RUN venv/bin/pip install --upgrade pip setuptools wheel

# copy setup.py
COPY setup.py .

# install requirements
RUN venv/bin/pip install --no-cache-dir .

# -------------------------------------------------------------- release stage

# runtime image
FROM python:3.8-alpine

# set runtime working directory
WORKDIR /app

# install runtime dependencies
RUN apk add --no-cache postgresql-libs

# copy built packages
COPY --from=builder /app .

# copy project files
COPY . .

# set path to use built packages
ENV PATH="/app/venv/bin:$PATH"

# write python output immediately to the stdout
ENV PYTHONUNBUFFERED 1

# don't create .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# expose port to the outside
EXPOSE 8080

# run it!
CMD ["./start-all.sh"]
