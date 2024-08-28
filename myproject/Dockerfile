# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Expose the port that the app runs on
EXPOSE 8000

# Run tests and then start Django's development server
CMD ["sh", "-c", "python manage.py test && python manage.py runserver 0.0.0.0:8000"]
