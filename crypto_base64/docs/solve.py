import base64
from pathlib import Path

with open(Path(__file__).parent.parent / "attachments" / "base64.txt", "r") as f:
    flag = f.read()

while True:
	flag = base64.b64decode(flag)
	flagStr = flag.decode("utf-8")
	if "sunctf" in flagStr:
		print(flagStr)
		break
