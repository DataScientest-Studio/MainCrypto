# Utilisez l'image Python 3.12.4 basée sur Ubuntu 22.04
FROM python:3.12.4-slim-bullseye

# pip installation
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    && pip install --upgrade pip \
    && pip install tensorflow \
    && pip install mlflow \
    && pip install psycopg2-binary \
    && pip install pytest \
    # && pip install apache-airflow \
    && pip install statsd \
    && pip install requests \
    && pip install --upgrade typing_extensions \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*