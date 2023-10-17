# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set the working directory to /app
WORKDIR /workdir

# Copy the current directory contents into the container at /app
COPY . /workdir

# Install any dependencies
RUN pip install -r /workdir/DataCleaning/requirements.txt

ENTRYPOINT ["python", "/workdir/DataCleaning/main.py"]