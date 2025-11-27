FROM python:3.11-slim

WORKDIR /app

# Copy app folder
COPY app/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Use Python to run the app
CMD ["python", "app.py"]