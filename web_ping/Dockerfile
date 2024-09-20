FROM python:3.10-slim

WORKDIR /app

COPY ./app /app

RUN apt-get update && apt-get install -y curl iputils-ping && \
    pip install -r requirements.txt

RUN useradd -m ctfuser

RUN chown -R root:root /app && \
    chmod -R 755 /app

USER ctfuser

EXPOSE 5004

CMD [ "python3", "app.py" ]
