# Use a lightweight Python base
FROM python:3.11-slim

# Create app directory
WORKDIR /app
ENV PYTHONPATH="/app"

# Copy code
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Port for Django app
EXPOSE 8000

# Start gunicorn server
CMD ["gunicorn", "backend.backend.wsgi:application", "--bind", "0.0.0.0:8000"]
