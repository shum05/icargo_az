# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any other Python packages you need from requirements.txt
RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt

# Specify the command to run when the container starts
CMD ["python3", "app.py"]
