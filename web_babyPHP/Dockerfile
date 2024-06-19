FROM php:8.1-apache

RUN apt-get update && apt-get install -y 

RUN sed -i 's/Listen 80/Listen 5002/' /etc/apache2/ports.conf

COPY index.php /var/www/html/




