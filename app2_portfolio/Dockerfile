# Dockerfile

# Use the official Python image (includes ARM compatibility)
FROM python:3.10.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the application files into the container
COPY . /app/

# Install necessary dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 8501 for Streamlit
EXPOSE 8501

# Healthcheck to verify application health
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Entry point to run the Streamlit application
ENTRYPOINT ["streamlit", "run", "src/Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
