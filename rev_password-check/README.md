# Password Check

| Key            | Value                                                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Challenge Name | Password Check                                                                                                                                                                              |
| Author         | Wowiee3                                                                                                                                                                                     |
| Category       | Rev                                                                                                                                                                                         |
| Description    | I hear its amazing when the famous purple stuffed worm in flap-jaw space with the tuning fork does a raw blink on Hara Kiri Rock.<br><br>Flag format: `sunctf{correct_password}`.      |
| Challenge Type | Static                                                                                                                                                                                      |
| Flag           | sunctf{ineedscissors61}                                                                                                                                                                     |
| Score          | 100                                                                                                                                                                                         |

*File(s) in `attachments/` are distributed to the participants.*

*Hint: The password is stored as a string.*

## Solution

<details>
<summary>Click to expand</summary>

Password is still 'stringable', it's just less obvious. Or you can reverse it as well. See `docs/decompiled.c` for the
code decompiled by BinaryNinja. Either method will give you the password and plaintext flag.

</details>

Note: `docs/solve.py` can be used to check if the challenge is working as intended. It will solve the challenge and get
the flag.
