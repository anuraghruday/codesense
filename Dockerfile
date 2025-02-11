FROM python:3.9
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt
COPY backend /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]