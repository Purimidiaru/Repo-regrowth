# Use Python image (version 3.12.4)
FROM python:3.12.4-slim

# Install git
RUN apt-get update && apt-get install -y git && apt-get clean

# Create a non-root user and group
RUN groupadd -r appgroup && useradd -m -r -g appgroup appuser

# Set the working dir in the container
WORKDIR /usr/src/app

# Copy the requirements file in the container (Empty in that case)
COPY requirements.txt ./

# Install the dependencies from requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full app in the container
COPY . .

# Change ownership of the workdir
RUN chown -R appuser:appgroup /usr/src/app

# Specify the user
USER appuser

# Command to run the script
CMD ["python3", "tests/test_backup.py"]
