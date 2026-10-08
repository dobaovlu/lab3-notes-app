FROM python:3.12-slim

# Print logs immediately, so they show up in the Render Logs panel in order
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8000

# Lab 3, Task A: this port is hard-coded. Replace the line so the port
# comes from the PORT environment variable (handout, Task A step 1).
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
