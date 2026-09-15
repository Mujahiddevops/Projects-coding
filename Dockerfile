# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy repository files into the container
COPY . /app

# Run ledger.py when container starts
CMD ["python", "ledger.py"]
