# Dockerfile
FROM python:3.8

# Install required packages
RUN pip install requests

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Command to run the application
CMD ["python", "./debug.py"]  # Run the debug.py script
