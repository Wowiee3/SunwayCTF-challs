FROM php:8.1-apache

RUN apt-get update && apt-get install -y 

RUN sed -i 's/Listen 80/Listen 5000/' /etc/apache2/ports.conf

EXPOSE 5000
COPY src /var/www/html/
