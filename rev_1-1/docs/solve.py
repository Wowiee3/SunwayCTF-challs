from socket import *
import re


with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 8889))

    s.recv(1024)

    key = 'ECCO2K'
    assert sum(map(ord, key)) == 407
    s.sendall((key + '\n').encode())

    ret = s.recv(1024)
    flag = re.search(r'sunctf{.*?}', ret.decode())
    print(flag.group())
