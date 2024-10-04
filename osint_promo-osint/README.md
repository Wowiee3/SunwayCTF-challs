# Promo OSINT

| Key            | Value                                                                                     |
|----------------|-------------------------------------------------------------------------------------------|
| Challenge Name | Promo OSINT                                                                               |
| Author         | Wowiee3                                                                                   |
| Category       | OSINT                                                                                     |
| Description    | Can you find the hidden flag in our promotion post for this CTF?<br>Hint: It's encrypted! |
| Challenge Type | Static                                                                                    |
| Flag           | sunctf{b4z1ng4}                                                                           |
| Score          | 100                                                                                       |

## Solution

<details>
<summary>Click to expand</summary>

Super ez social media OSINT. Flag is hidden in a line of text in the promo post on CSC's instagram, encoded in base64.

![The instagram post](docs/post.png)

```python
>>> from base64 import b64decode
>>> b64decode('c3VuY3Rme2I0ejFuZzR9')
b'sunctf{b4z1ng4}'
```

</details>
