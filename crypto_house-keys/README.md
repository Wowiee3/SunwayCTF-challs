# House Keys

| Key            | Value                                                                                                   |
|----------------|---------------------------------------------------------------------------------------------------------|
| Challenge Name | House Keys                                                                                              |
| Author         | warlocksmurf                                                                                            |
| Category       | Crypto                                                                                                  |
| Description    | Dr House encrypted the flag with his public key, but he accidentally left his private key on the table. |
| Challenge Type | Static                                                                                                  |
| Flag           | sunctf{d0ct0r_h0us3_l0st_h1s_k3ys}                                                                      |
| Score          | ???                                                                                                     |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

1) Decrypt the encrypted flag with the private key given.

   ```commandline
   openssl pkeyutl -decrypt -inkey private_key.pem -in flag.txt.enc -out flag.txt
   ```

   Or you can do with a script.
</details>

Note: `docs/solve.py` can be used to check if the challenge is working as intended. It will solve the challenge and get
the flag.
