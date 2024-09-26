from pathlib import Path
import re

with open(Path(__file__).parent.parent / 'attachments' / 'stringsme', 'rb') as f:
    dump = f.read()

flag = re.search(r'sunctf{.*?}', str(dump))
print(flag.group())
