# Use a stable Airflow version
FROM apache/airflow:2.7.1-python3.11

# Switch to root to install optional packages
USER root
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Switch back to airflow user
USER airflow

# Set working directory
WORKDIR /opt/airflow

# Install provider packages from requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
