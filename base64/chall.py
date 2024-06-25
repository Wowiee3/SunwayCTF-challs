import base64

flag = "SUNCTF{did_you_script_this?}"
flag = flag.encode("ascii")
for x in range(32):
	flag = base64.b64encode(flag)
f = open("base64.txt", "w")
f.write(flag.decode("utf-8"))
f.close()
