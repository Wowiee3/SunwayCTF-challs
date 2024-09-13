from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import bytes_to_long, long_to_bytes
import os

flag = "sunctf{FAKEFLAG}"

key = os.urandom(AES.key_size[0])
iv = os.urandom(AES.block_size)
secret = flag.encode()

def encrypt(pt):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_pt = pad(pt, AES.block_size)
    ciphertext = cipher.encrypt(padded_pt)
    return ciphertext

ciphertext_secret = encrypt(secret)

print("=============================================")
print(f"Key: {key.hex()}")
print(f"IV: {iv.hex()}")
print(f"Encrypted flag: {ciphertext_secret.hex()}")
print("=============================================")
