FROM jaredliw/base_image_nginx_mysql_php_54

RUN sed -i 's/listen[[:space:]]\+80;/listen 5004;/g' /etc/nginx/nginx.conf

EXPOSE 5004
COPY src /var/www/html
