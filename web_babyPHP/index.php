<?php
error_reporting(0);

highlight_file(__FILE__);

$username = $_GET['username'];
$key = $_GET['key'];

if (gettype($username) === 'string' || is_null($username)){
    echo "You need to supply the correct parameters!";
    die();
}

if ($key === "HTTP_PARAMS"){
    echo "<pre>";
    echo "sunctf{w0w_aRrrays_are_all0wed}";
    echo "</pre>";
    die();
}
echo "You need to supply the correct parameters!";
?>

