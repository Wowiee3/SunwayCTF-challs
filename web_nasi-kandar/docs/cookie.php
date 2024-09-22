<?php

class Plate{
    public $squid;
    public $fried_chicken;
    public $cabbage;
    public $fish;
    public $salted_egg;
    public $price;
    public $boss_calculation;

    function __construct($squid, $fried_chicken, $cabbage, $fish, $salted_egg, $price){
        $this->squid = $squid;
        $this->fried_chicken = $fried_chicken;
        $this->cabbage = $cabbage;
        $this->fish = $fish;
        $this->salted_egg = $salted_egg;
        $this->price = $price;
    }
}

$user = new Plate(1,1,1,1,1,true);
$b64price = base64_encode(serialize($user));
echo $b64price;