import base64

f = open("base64.txt", "r")
flag = f.read()

while True:
	flag = base64.b64decode(flag)
	flagStr = flag.decode("utf-8")
	if "SUN" in flagStr:
		print(flagStr)
		break
