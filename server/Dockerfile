FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server code
COPY . .

# Copy the model from the current directory
COPY model1.p /model1.p
# And update app.py to look in /model1.p or use an env var.

ENV MODEL_PATH=/model1.p

EXPOSE 5000

CMD ["python", "app.py"]
