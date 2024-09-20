<?php
error_reporting(0);
$servername = "127.0.0.1";
$username = "root";
$password = "root";
$dbname = "redacted";

$conn = mysqli_connect($servername, $username, $password, $dbname);
//if (!$conn) {
//    die('Could not connect: ' . mysqli_error($conn));
//}
