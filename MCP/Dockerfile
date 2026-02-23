# Use a Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files to the container
COPY . /app/

# Expose the port MCP server will run on
EXPOSE 8080

# Run FastMCP server (adjust to your entrypoint)
CMD ["python", "server.py"]