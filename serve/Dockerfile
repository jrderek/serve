FROM python:3.8-slim

WORKDIR /app
COPY . .

RUN pip install fastapi pandas

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
