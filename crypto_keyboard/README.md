# Keyboard

| Key            | Value                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------------|
| Challenge Name | Keyboard                                                                                                                         |
| Author         | wolfishLamb                                                                                                                      |
| Category       | Crypto                                                                                                                           |
| Description    | What's wrong with my keyboard?<br><br>Decrypt `cipher.txt`. The last word in the file is your flag, submit it as `sunctf{word}`. |
| Challenge Type | Static                                                                                                                           |
| Flag           | sunctf{nowiknowmyabc}                                                                                                            |
| Score          | 200                                                                                                                              |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

The text is encrypted by an easy 1-to-1 substitution. Perform a frequency analysis to get back the plain text.

</details>

Note: `attachments/cipher.txt` was generated from `docs/chall.py`.

P.S.: The short passage was taken from
the [Sunway A Level brochure](https://sunwaycollege.edu.my/sites/default/files/documents/A%20LEVEL%20Student%20Guide%202024.pdf),
acting as a tribute to my miserable year in the A-Level program.
