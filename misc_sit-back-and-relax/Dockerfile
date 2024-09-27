FROM python:3.8-alpine

RUN pip install flask

WORKDIR /app
COPY src/ /app/

EXPOSE 1338
CMD ["python3", "app.py"]
