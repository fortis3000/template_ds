# Use the official Python image as a base
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install uv, our package manager
RUN pip install uv

# Copy the dependency files
COPY pyproject.toml uv.lock ./

# Install the project dependencies using uv
RUN uv pip sync

# Copy the source code into the container
COPY src/ ./src/

# Default command to run when the container starts
CMD ["bash"]
