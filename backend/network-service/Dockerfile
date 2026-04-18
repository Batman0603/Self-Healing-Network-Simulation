FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY network-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY network-service/ .
COPY shared/ ./shared/

ENV PYTHONPATH=/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]