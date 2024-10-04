# Stringsme

| Key            | Value                                                                                     |
|----------------|-------------------------------------------------------------------------------------------|
| Challenge Name | Stringsme                                                                                 |
| Author         | Wowiee3                                                                                   |
| Category       | Rev                                                                                       |
| Description    | Here's a little executable file for you. Can you find the flag using the strings command? |
| Challenge Type | Static                                                                                    |
| Flag           | sunctf{us3str1ng5}                                                                        |
| Score          | 50                                                                                        |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

Ez rev chall, just `strings` the `stringsme.exe` file, or you can search for printable characters with a script.

```
strings stringsme | grep sunctf
```

</details>

Note: `docs/solve.py` can be used to check if the challenge is working as intended. It will solve the challenge and get
the flag.
