# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set the working directory to /app
WORKDIR /DataCleaning

# Copy the current directory contents into the container at /app
COPY . /DataCleaning

# Install any dependencies
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]