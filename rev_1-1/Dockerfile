FROM ubuntu:latest

WORKDIR /usr/src/app
COPY src/ /usr/src/app/

RUN apt-get update && apt-get install -y socat

EXPOSE 8889
CMD ["socat", "TCP-LISTEN:8889,reuseaddr,fork", "EXEC:./crackme"]
