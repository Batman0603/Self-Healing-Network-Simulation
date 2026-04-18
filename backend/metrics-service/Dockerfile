FROM python:3.11-slim
WORKDIR /app

COPY metrics-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY metrics-service/ .
COPY shared/ ./shared/

ENV PYTHONPATH=/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8012"]