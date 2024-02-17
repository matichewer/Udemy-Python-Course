# Dockerfile

# Use the official Python image (includes ARM compatibility)
FROM python:3.10.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the application files into the container
COPY . /app/

# Install necessary dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 5001 for Flask
EXPOSE 5001

CMD ["python", "app.py"]
