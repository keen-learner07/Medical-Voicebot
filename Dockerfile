# Use Python 3.13 slim image as base
FROM python:3.13-slim

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    portaudio19-dev \
    libasound2-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory in the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Gradio default port
EXPOSE 7860

# Start the app
CMD ["python", "gradio_app.py"]
