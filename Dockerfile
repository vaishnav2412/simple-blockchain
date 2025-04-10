# Use an official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "main.py"]

