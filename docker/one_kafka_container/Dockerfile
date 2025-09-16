# Use an official Python runtime as a parent image
FROM python:latest

#Labels as key value pair
LABEL Maintainer="alexey.me"

# Set the working models in the container to /app
WORKDIR /usr/app/src

# Copy the current models contents into the container at /app
COPY .. ./

# Install any required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run your application
CMD ["python", "kafka_producer.py"]