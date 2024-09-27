# Loong

| Key            | Value                                              |
|----------------|----------------------------------------------------|
| Challenge Name | Packman                                            |
| Author         | warlocksmurf                                       |
| Category       | Rev                                                |
| Description    | Why does my script pack up his snacks before work? |
| Challenge Type | Static                                             |
| Flag           | sunctf{Pyth0n_fr0m_zZz_0r_c0de}                    |
| Score          | ???                                                |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

1) The executable is packed with PyInstaller, depack it will provide a suspicious `packman.pyc` file. See
   `docs/packman.exe_extracted.zip`.

2) The `packman.pyc` file can be decompiled with tools and online websites to uncover the malicious script. See
   `docs\packman_pyc_decompiled.py`.

3) From the script you can see the flag, `8cbb8acce9e5a6ffd9e858891a57876dfa3a4e49b71309b928d134ae40ad8f79`, is
   encrypted with AES key `536e616b6548617465734c616464657273496e4d79496e666f537465616c6572`. Copy and run the
   `decrypt_flag` function with these values.

</details>

Note: `docs/solve.py` can be used to check if the challenge is working as intended. It will solve the challenge and get
the flag.