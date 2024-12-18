# Use an official Python base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for Python packages (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your Gunicorn app will run on
EXPOSE 5000

# Set the command to run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
