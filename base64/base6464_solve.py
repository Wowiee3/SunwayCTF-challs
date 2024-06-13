import base64

f = open("base64.txt", "r")
flag = f.read()

for x in range(32):
	flag = base64.b64decode(flag)
print(flag.decode("utf-8"))