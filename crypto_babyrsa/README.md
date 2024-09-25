# babyRSA

| Key            | Value                                                         |
|----------------|---------------------------------------------------------------|
| Challenge Name | babyRSA                                                       |
| Author         | SuperTsumu                                                    |
| Category       | Crypto                                                        |
| Description    | Obligatory RSA challenge. `n` is only 256 bits, you got this. |
| Challenge Type | Static                                                        |
| Flag           | sunctf{did_you_listen_in_class?}                              |
| Score          | ???                                                           |

File(s) in `attachments/` are distributed to the participants.

## Solution

<details>
<summary>Click to expand</summary>

Factor `n` using [factordb.com](factordb.com) then decrypt the message in the standard RSA way.

</details>

Note: `docs/solve.py` can be used to check if the challenge is working as intended. It will solve the challenge and get
the flag.

Note: `attachments/babyRSA.txt` is generated using `docs/chall.py`.
