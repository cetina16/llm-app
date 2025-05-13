# Use the official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN apt-get update && apt-get install -y \
    cmake \
    pkg-config \
    libprotobuf-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the application code to the container
COPY . /app

# Expose the port Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
