FROM php:8.1-apache

RUN apt-get update && apt-get install -y 

RUN sed -i 's/Listen 80/Listen 5000/' /etc/apache2/ports.conf

COPY index.html /var/www/html/

COPY robots.txt /var/www/html/

COPY flag.php /var/www/html/
COPY codeGen.php /var/www/html/




