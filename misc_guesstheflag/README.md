# guessTheFlag

| Key            | Value                                                                                                                               |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Challenge Name | guessTheFlag                                                                                                                        |
| Author         | SuperTsumu                                                                                                                          |
| Category       | Misc                                                                                                                                |
| Description    | Find a way to bruteforce faster than your peers.                                                                                    |
| Challenge Type | Dynamic Docker                                                                                                                      |
| Docker Image   | [jaredliw/sunctf_misc_guesstheflag](https://hub.docker.com/repository/docker/jaredliw/sunctf_misc_guesstheflag/general) (port 8888) |
| Flag           | sunctf{c4n7_7h1nk_0f_fl46_n4m35}                                                                                                    |
| Score          | 400                                                                                                                                 |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

It is a good solution as long as you get the flag. See [how we solve it](docs/solve.py).
</details>

Warn: If you are trying to build and run the container from scratch, make sure that you are using LF in
`src/guessTheFlag.sh` to prevent error.

Note: `docs/solve.py` can be used to check if the challenge is working as intended. It will solve the challenge and get
the flag.
