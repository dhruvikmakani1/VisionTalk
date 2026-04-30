FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server code
COPY . .

# Copy the model from the current directory
COPY model1.p /model1.p

ENV MODEL_PATH=/model1.p

EXPOSE 8000

# Use gunicorn for production — reads PORT env var (default 8000 on Koyeb)
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120 app:app"]
