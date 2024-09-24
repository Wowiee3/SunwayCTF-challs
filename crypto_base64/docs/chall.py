import base64
from pathlib import Path

flag = "sunctf{did_you_script_this?}"
flag = flag.encode("ascii")
for x in range(32):
	flag = base64.b64encode(flag)

with open(Path(__file__).parent.parent / "attachments" / "base64.txt", "w") as f:
    f.write(flag.decode("utf-8"))
