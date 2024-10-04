from pathlib import Path
from base64 import b16decode


with open(Path(__file__).parent.parent / 'attachments' / 'flag.txt', 'r') as f:
	flag = f.read()

print(b16decode(flag, casefold=True).decode())
