<?php
error_reporting(0);
session_start(); 


if (!isset($_SESSION['logged'])) {
    header("Location: index.php");
    exit();
}

class Plate{
    public $squid;
    public $fried_chicken;
    public $cabbage;
    public $fish;
    public $salted_egg;
    public $price;

    function __construct($squid, $fried_chicken, $cabbage, $fish, $salted_egg, $price){
        $this->squid = $squid;
        $this->fried_chicken = $fried_chicken;
        $this->cabbage = $cabbage;
        $this->fish = $fish;
        $this->salted_egg = $salted_egg;
        $this->price = $price;
    }
}

if ($_SERVER['REQUEST_METHOD'] == "POST"){
    try{
        $squid = isset($_POST['sotong']) ? (int)$_POST['sotong'] : 0;
        $fried_chicken = isset($_POST['ayam_goreng']) ? (int)$_POST['ayam_goreng'] : 0;
        $cabbage = isset($_POST['kobis']) ? (int)$_POST['kobis'] : 0;
        $fish = isset($_POST['ikan']) ? (int)$_POST['ikan'] : 0;
        $salted_egg = isset($_POST['telur_masin']) ? (int)$_POST['telur_masin'] : 0;
        $price = isset($_POST['price']) ? (int)$_POST['price'] : 0;
        
        $user = new Plate($squid, $fried_chicken, $cabbage, $fish, $salted_egg, $price);
        $b64price = base64_encode(serialize($user));
        setcookie("guessed_price", $b64price);

        header("Location: /price.php");
        die();

    }catch(Exception $e){
        echo 'Error: ',  $e->getMessage(), "\n";
        die();
    }
    
}

if ($_SERVER['REQUEST_METHOD'] == "GET"){
    if(isset($_COOKIE['guessed_price'])){
        try{
            //Random because it depends on his mood :D
            $boss_calculation = random_int(1,2147483647);

            $user_list = unserialize(base64_decode($_COOKIE['guessed_price']));

            $guessed_price = $user_list->price;

            if ($guessed_price == $boss_calculation){
                echo "sunctf{mySQL_is_insensItive_strict_is_the_B3st}";
            }else{
                echo "Wrong price";
            }

        }catch(Exception $e){
            echo 'Error: ',  $e->getMessage(), "\n";
            die();
        }
        
    }else{
        echo "Cookie not set";
    }
}
?>