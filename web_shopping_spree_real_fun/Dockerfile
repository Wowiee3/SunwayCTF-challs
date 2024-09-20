FROM python:3.8-alpine

WORKDIR /app

COPY ./ /app/

RUN pip install -r /app/requirements.txt

CMD ["sh", "-c", "python3 init_db.py && python3 app.py"]