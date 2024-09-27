from requests import request
import re

res = request(url="http://localhost:1338", method="BREW")

flag = re.search(r'sunctf{.*?}', res.text)
print(flag.group())
