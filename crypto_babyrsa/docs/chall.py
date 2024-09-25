from math import gcd
from Crypto.Util.number import *  # pip install pycryptodome

# Step 1: pick two large prime numbers, p and q
p = 331479022735552987490170086096526015841
q = 323167587041971366655979066198678700897
assert isPrime(p) and isPrime(q)
print(f'{p = }')
print(f'{q = }')

# Step 2: compute n = p * q
n = p * q
print(f'{n = }')

# Step 3: compute Euler's totient function, 'phi(n) = (p - 1) * (q - 1),
#         i.e. the number of integers less than n that are coprime to n (incl. 1)
phi = (p - 1) * (q - 1)
print(f'{phi = }')

# Step 4: pick an e such that 1 < e < phi(n) and e is coprime to phi(n)
e = 65537  # public key: (e, n)
assert 1 < e < phi and gcd(e, phi) == 1
print(f'{e = }')

# Step 5: compute d such that e * d = 1 (mod phi(n))
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b%a,a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m
    
d = modinv(e, phi)  # private key: (d, n)
assert (e * d) % phi == 1
print(f'{d = }')

# Step 6: encrypt the message
m = "sunctf{did_you_listen_in_class?}"

def encrypt(e, n, plaintext):
    key, n = e, n
    plaintext_bytes = plaintext.encode('utf-8')
    plaintext_int = bytes_to_long(plaintext_bytes)
    print(f'\nm = {plaintext_int}')
    cipher_int = pow(plaintext_int, key, n)
    return cipher_int

c = encrypt(e, n, m)
print(f'{c = }')

# Step 7: decrypt the message
flag = long_to_bytes(pow(c, d, n)).decode()
assert flag == m
print(f'{flag = }')

if __name__ == '__main__':
    from pathlib import Path

    with open(Path(__file__).parent.parent / 'attachments' / 'babyRSA.txt', 'w') as f:
        f.write(f'{n = }\n')
        f.write(f'{e = }\n')
        f.write(f'{c = }')
