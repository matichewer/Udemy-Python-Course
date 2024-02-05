# Dockerfile

# Use the official Python image (includes ARM compatibility)
FROM python:3.10.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY src/requirements.txt /app/

# Copy the Streamlit application files into the container
COPY src/web.py /app/
COPY src/functions.py /app/
COPY src/todos.txt /app/

# Install necessary dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 8501 for Streamlit
EXPOSE 8501

# Healthcheck to verify application health
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Entry point to run the Streamlit application
ENTRYPOINT ["streamlit", "run", "web.py", "--server.port=8501", "--server.address=0.0.0.0"]
