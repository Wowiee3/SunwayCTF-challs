from pathlib import Path
import subprocess
import re


process = subprocess.Popen(
    str(Path(__file__).parent.parent / 'attachments' / 'loong.exe'),
    shell=True, text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE
)
stdout, stderr = process.communicate(input='ghidra')

flag = re.search(r'sunctf{.*?}', stdout)
print(flag.group())
