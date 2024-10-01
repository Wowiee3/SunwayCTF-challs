#!/bin/sh

mysqld_safe &

mysql_ready() {
	mysqladmin ping --socket=/run/mysqld/mysqld.sock --user=root --password=root > /dev/null 2>&1
}

while !(mysql_ready)
do
	echo "waiting for mysql ..."
	sleep 3
done

if [[ -f db.sql ]]; then
    mysql -e "source db.sql" -uroot -proot
    rm -f db.sql
fi

npm run start