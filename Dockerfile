# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to the project root
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Apply migrations
RUN python manage.py migrate

# Set environment variables
ENV NAME=World
ENV DJANGO_SETTINGS_MODULE=confi.settings
ENV PORT=8000

# Expose the port the app runs on
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
