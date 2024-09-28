from pathlib import Path

with open(Path(__file__).parent.parent / 'attachments' / 'rottenflag.txt', 'r') as f:
    content = f.read().rstrip()


for shift in range(26):
    shifted = ''.join(map(lambda x: chr(ord(x) + shift), content))

    if 'sunctf' in shifted:
        print(shifted)
        break
