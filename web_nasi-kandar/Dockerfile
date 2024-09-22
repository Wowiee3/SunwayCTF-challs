# Only one container is allowed for each challenge
FROM ctftraining/base_image_nginx_mysql_php_73:latest

RUN rm -f /var/www/html/flag.sh
COPY src /var/www/html/
