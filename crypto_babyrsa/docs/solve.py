from pathlib import Path

from Crypto.Util.number import long_to_bytes  # pip install pycryptodome
from sympy import mod_inverse  # pip install sympy

with open(Path(__file__).parent.parent / 'attachments' / 'babyRSA.txt', 'r') as f:
    exec(f.read())  # n, e and c are defined from now on

# Check factordb.com to get p and q
p = 323167587041971366655979066198678700897
q = 331479022735552987490170086096526015841

# Compute phi(n)
phi = (p - 1) * (q - 1)

# Compute d
d = mod_inverse(e, phi)

# decrypt message
m = pow(c, d, n)
print(long_to_bytes(m).decode())
