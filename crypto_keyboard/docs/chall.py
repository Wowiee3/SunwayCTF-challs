from pathlib import Path
from random import shuffle, seed
from string import ascii_lowercase

this_dir = Path(__file__).parent
with open(this_dir / 'raw.txt', 'r') as f:
    content = f.read()

seed(23034218)
mapped = list(ascii_lowercase)
shuffle(mapped)

with open(this_dir.parent / 'attachments' / 'keyboard.txt', 'w') as f:
    for char in content:
        if char not in ascii_lowercase:
            f.write(char)
        else:
            f.write(mapped[ord(char) - ord('a')])
