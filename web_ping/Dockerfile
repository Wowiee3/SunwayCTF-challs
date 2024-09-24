FROM python:3.10-slim

WORKDIR /app

COPY ./src /app

RUN apt-get update && apt-get install -y curl iputils-ping && \
    pip install -r requirements.txt

RUN useradd -m ctfuser

RUN chown -R root:root /app && \
    chmod -R 755 /app

USER ctfuser

EXPOSE 5006

CMD [ "python3", "app.py" ]
