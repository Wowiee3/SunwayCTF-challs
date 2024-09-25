from pathlib import Path
from Crypto.Cipher import AES  # pip install pycryptodome
from Crypto.Util.Padding import unpad

with open(Path(__file__).parent.parent / 'attachments' / 'babyAES.txt', 'r') as f:
    exec(f.read())  # key, iv and flag are defined from now on

key = bytes.fromhex(key)
iv = bytes.fromhex(iv)
flag = bytes.fromhex(flag)


# Decrypt function (AES in CBC mode)
def decrypt(ct):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(ct)
    return unpad(decrypted_bytes, AES.block_size).decode()


print(decrypt(flag))
