from pathlib import Path
from Crypto.PublicKey import RSA  # pip install pycryptodome
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Random import get_random_bytes

base_path = Path(__file__).parent.parent / 'attachments'

with open(base_path / 'flag.txt.enc', 'rb') as f:
    enc = f.read()
with open(base_path / 'private_key.pem', 'r') as f:
    key = RSA.import_key(f.read())

cipher_rsa = PKCS1_v1_5.new(key)
flag = cipher_rsa.decrypt(enc, get_random_bytes(16)).decode()
print(flag)
