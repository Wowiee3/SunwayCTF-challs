from pathlib import Path

with open(Path(__file__).parent.parent / 'attachments' / 'flag.txt') as f:
    content = f.read()

    for idx in range(0, len(content), 9):
        binary = content[idx:idx+8]
        ascii = chr(int(binary, 2))
        print(ascii, end='')

    print()
