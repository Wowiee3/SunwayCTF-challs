<?php
define('DB_SERVER', 'mysql');
define('DB_USERNAME', 'user');
define('DB_PASSWORD', 'tester');
define('DB_NAME', 'tester');

$db_connection = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME, 3306);

if($db_connection === false){
    die("ERROR: Could not connect to DB " . mysqli_connect_error());
}

?>