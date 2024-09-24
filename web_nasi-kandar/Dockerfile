# Only one container is allowed for each challenge
FROM ctftraining/base_image_nginx_mysql_php_73:latest

RUN rm -f /var/www/html/flag.sh \
    && sed -i 's/listen[[:space:]]\+80;/listen 5002;/g' /etc/nginx/nginx.conf


EXPOSE 5002
COPY src /var/www/html/
