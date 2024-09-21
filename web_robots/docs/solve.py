import requests

URL = "http://localhost:5000/flag.php"

VALUE = "361586575"

data = {
    "code": VALUE
}

r = requests.post(URL, data=data)

print(r.text)
