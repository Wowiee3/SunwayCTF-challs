FROM ubuntu:latest

WORKDIR /usr/src/app
COPY src/ /usr/src/app/

RUN apt-get update && apt-get install -y socat

EXPOSE 8888
CMD ["socat", "TCP-LISTEN:8888,reuseaddr,fork", "EXEC:./guessTheFlag.sh"]
