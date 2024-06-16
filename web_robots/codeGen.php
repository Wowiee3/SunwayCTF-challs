<?php

$seed = 16062024;

mt_srand($seed);

for ($i = 0; $i <= 100; $i++){
    $secretcode = mt_rand();
}

highlight_file(__FILE__);
?>

