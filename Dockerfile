FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
#RUN pip install --no-cache-dir fastapi uvicorn[standard] transformers torch

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.service.api:app", "--host", "0.0.0.0", "--port", "8000"]
