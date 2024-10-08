# Robots

| Key            | Value                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------|
| Challenge Name | Schools                                                                                                                 |
| Author         | chuajianshen                                                                                                            |
| Category       | Web                                                                                                                     |
| Description    | I protected my environment keys and prevented malicious file reads from Sunway hackers!                                 |
| Challenge Type | Static Docker                                                                                                           |
| Docker Image   | [jaredliw/sunctf_web_schools](https://hub.docker.com/repository/docker/jaredliw/sunctf_web_schools/general) (port 5001) |
| Flag           | sunctf{ea5h_pr0cess_ha5_1ts_oWn_PID}                                                                                    |
| Score          | 200                                                                                                                     |

*File(s) in `attachments/` are distributed to the participants.*

![Screenshot](docs/screenshot.png)

## Solution

<details>
<summary>Click to expand</summary>

Things to know:

- Each running program has a corresponding process ID (PID).
- In Linux, `/proc` is a virtual filesystem that presents information about processes. You can access the environment
  variables of a process by reading `/proc/<PID>/environ`.

1) As the challenge description hints, we should search for the flag in the environment variables. Therefore,
   `/proc/1/environ` file is the target. The `1` refers to the PID of the init process.

   If the `self` keyword is not banned in `app.js`, `/proc/self/environ` is an equivalent way to do this. `/proc/self`
   is a symbolic link to the directory for the current process, no matter what the PID is.
2) Here the flaw comes in. The path filtering on `../` is done non-recursively, and can be bypassed using
   patterns like `....//` or `..././`, which are both reduced to `../`. We may leverage this to read arbitrary files by
   traversing up directories.
3) An example of a valid payload to read the flag would be `/file?school=....//....//proc/1/environ`.

> Related: *Path Traversal*

</details>

Warn: If you are using ctfd-whale, the plugin will write a generated flag to the ENV named `FLAG`. Overwrite this
behavior or avoid using `FLAG` in ENV to prevent the true flag getting overwritten.

Note: `docs/solve.py` can be used to check if the challenge is working as intended. It will solve the challenge and get
the flag.
