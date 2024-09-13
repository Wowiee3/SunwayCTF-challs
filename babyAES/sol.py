from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = bytes.fromhex("826cf418f07f78cb9bb37685f880cc3f")  # Replace with actual key
iv = bytes.fromhex("38fa8037d3043190c361499c0416c814")  # Replace with actual IV
ciphertext_secret = bytes.fromhex("03c30a5cc2ced7bc178f936bafae65342422edace2a127ae830d7c6c69a56d4aff052a325602f896b2770ee0374dba92")  # Replace with actual ciphertext

# Decrypt function (AES in CBC mode)
def decrypt(ct):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(ct)
    return unpad(decrypted_bytes, AES.block_size).decode()

flag = decrypt(ciphertext_secret)
print(f"Decrypted flag: {flag}")
