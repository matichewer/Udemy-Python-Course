# Use the official Python image (includes ARM compatibility)
FROM python:3.10.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install necessary dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Execute migrations
#RUN python manage.py migrate

# Create a superuser non-interactively
#ENV DJANGO_SUPERUSER_USERNAME=admin
#ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
#ENV DJANGO_SUPERUSER_PASSWORD=cambiaestaclave123

#RUN python manage.py createsuperuser                \
#        --noinput                                   \
#        --username $DJANGO_SUPERUSER_USERNAME       \
#        --email $DJANGO_SUPERUSER_EMAIL

# Expose port  8000 for Django development server
EXPOSE  8000

# Entry point to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
