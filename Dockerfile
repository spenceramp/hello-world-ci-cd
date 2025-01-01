# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /opt

# Install Flask dependency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 8080
EXPOSE 8080

# Command to run the app
CMD ["python3", "app.py"]