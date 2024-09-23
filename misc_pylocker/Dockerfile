FROM python:3.9-slim

WORKDIR /usr/src/app
COPY src/ /usr/src/app/

RUN apt-get update && apt-get install -y socat

EXPOSE 1337
CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:'python main.py'"]
