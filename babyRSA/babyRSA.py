from Crypto.Util.number import *
p = 331479022735552987490170086096526015841
q = 323167587041971366655979066198678700897
n = p * q
print("n: " + str(n))
e = 65537
m = "SUNCTF{did_you_listen_in_class?}"
totient = (p - 1) * (q - 1)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m
    
d = modinv(e, totient)

def encrypt(e, n, plaintext):
    key, n = e, n
    plaintext_bytes = plaintext.encode('utf-8')
    plaintext_int = bytes_to_long(plaintext_bytes)
    cipher_int = pow(plaintext_int, key, n)
    return cipher_int

c = encrypt(e, n, m)
print("enc: " + str(c))
flag = pow(c, d, n)
print(long_to_bytes(flag))