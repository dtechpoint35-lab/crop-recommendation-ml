FROM python:3.11-slim

WORKDIR /app/app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app /app/app
COPY models /app/models
COPY data /app/data

EXPOSE 5000

CMD ["python", "flask_app.py"]