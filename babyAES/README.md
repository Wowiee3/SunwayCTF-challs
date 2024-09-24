# babyAES

| Key            | Value                                                             |
|----------------|-------------------------------------------------------------------|
| Challenge Name | babyAES                                                           |
| Author         | warlocksmurf                                                      |
| Category       | Crypto                                                            |
| Description    | I assume you paid attention during cryptography classes?          |
| Challenge Type | Static                                                            |
| Flag           | sunctf{l34rn_y0ur_AES_b4s1cs_1n_cl4ss}                            |
| Score          | ???                                                               |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

1) Decrypt the flag with AES

```python
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
```

</details>

Note: `docs/solve.py` can be used to check if the challenge is working as intended. It will solve the challenge and get
the flag.
