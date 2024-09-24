FROM python:3.8-alpine

WORKDIR /app

COPY src/ /app/

RUN pip install -r /app/requirements.txt

EXPOSE 5003
CMD ["sh", "-c", "python3 init_db.py && python3 app.py"]
