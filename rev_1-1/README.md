# 1:1

| Key            | Value                                                                                                                                                               |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Challenge Name | 1:1                                                                                                                                                                 |
| Author         | Wowiee3                                                                                                                                                             |
| Category       | Rev                                                                                                                                                                 |
| Description    | You need a valid key to get the flag. 'Valid' and 'correct' aren't the same thing, though...<br>It's recommended to use a disassembler/debugger for this challenge. |
| Challenge Type | Static Docker                                                                                                                                                       |
| Docker Image   | sunctf_rev_1-1 (port 8889)                                                                                                                                          |
| Flag           | sunctf{not_the_only_1}                                                                                                                                              |
| Score          | 200                                                                                                                                                                 |

*File(s) in `attachments/` are distributed to the participants.*

*Hint: Release the obfuscated source code midway through the competition.*

## Solution

<details>
<summary>Click to expand</summary>

Decompile the executable (see `docs/decompiled.c`), we can see a `for` loop which sums up the characters we input.

```c
__isoc99_scanf(&DAT_00102043,local_88);
local_90 = 0;
local_8c = 0;
while( true ) {
    sVar1 = strlen(local_88);
    if (sVar1 <= (ulong)(long)local_8c) break;
    local_90 = local_90 + local_88[local_8c];
    local_8c = local_8c + 1;
}
```

(The counter is `local_8c` and the sum is `local_90`.)

Then the sum is compared to `0x197 = 407`.

```c
if (local_90 == 0x197) {
    puts("Valid key!");
    puts("Flag: <SEND TO SERVER TO GET THE FLAG.>");
}
```

Now we know what is going on in the code: the sum of all ASCII characters in the key must equal 407. Valid keys can be
made with a keygen. The key is not unique.

Original key used: `ECCO2K`.

</details>
