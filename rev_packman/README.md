# Loong

| Key            | Value                                          |
|----------------|------------------------------------------------|
| Challenge Name | Packman                                        |
| Author         | warlocksmurf                                   |
| Category       | Rev                                            |
| Description    | Why does my script pack up his snacks before work? |
| Challenge Type | Static                                         |
| Flag           | sunctf{Pyth0n_fr0m_zZz_0r_c0de}                |
| Score          | ???                                            |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

1) The executable is packed with PyInstaller, depack it will provide a suspicious `packman.pyc` file.

2) The `packman.pyc` file can be decompiled with tools and online websites to uncover the malicious script

3) The flag is encrypted with AES key `536e616b6548617465734c616464657273496e4d79496e666f537465616c6572`

</details>

Note: `docs/solve.py` can be used to check if the challenge is working as intended. It will solve the challenge and get
the flag.