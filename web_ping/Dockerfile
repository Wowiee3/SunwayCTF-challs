FROM python:3.10-slim

WORKDIR /app

COPY ./app /app

RUN apt-get update && apt-get install -y curl && \
    pip install -r requirements.txt

EXPOSE 5004

CMD [ "python3","app.py" ]
