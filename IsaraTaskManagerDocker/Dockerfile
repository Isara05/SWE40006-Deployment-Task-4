FROM python:3.13-slim

WORKDIR /app

# Prevent Python from creating .pyc files and enable immediate log output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Application configuration
ENV APP_ENV=production
ENV APP_PORT=5000

# Install dependencies separately to improve Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]