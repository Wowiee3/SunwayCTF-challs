FROM node:20-alpine

WORKDIR /usr/src/app
COPY src/ .

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk add --update --no-cache mysql mysql-client

RUN mysql_install_db --user=mysql --datadir=/var/lib/mysql \
    && sh -c 'mysqld_safe &' \
    && sleep 5s \
    && mysqladmin -uroot password 'root'

RUN npm install \
    && chmod +x start.sh

EXPOSE 5004

CMD ["/bin/sh", "-c", "./start.sh"]
