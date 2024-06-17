FROM python:3.8-alpine

WORKDIR /app

COPY ./ /app/

COPY ./flag.txt /flag.txt

RUN apk add curl

RUN rm /app/flag.txt

RUN pip install -r /app/requirements.txt

RUN adduser -D ctf
USER ctf

CMD ["python3", "app.py"] 