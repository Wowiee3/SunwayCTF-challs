from pathlib import Path
import subprocess


process = subprocess.Popen(
    str(Path(__file__).parent.parent / 'attachments' / 'password_check.exe'),
    shell=True, text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE
)

password = 'ineedscissors61'
stdout, stderr = process.communicate(input=password)

if "correct" in stdout:
    print(f'sunctf{{{password}}}')
