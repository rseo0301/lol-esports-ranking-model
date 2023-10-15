# Expects Docker build to be run from parent directory. We need this because we need to copy all code (eg. including models)

# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set the working directory to /app
WORKDIR /workdir

# Copy the current directory contents into the container at /app
COPY . /workdir

# Install any dependencies
RUN pip install -r /workdir/API/requirements.txt

# Expose ports
EXPOSE 5000

ENTRYPOINT ["python", "API/main.py", "--production"]