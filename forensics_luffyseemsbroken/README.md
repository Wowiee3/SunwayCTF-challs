# LuffySeemsBroken

| Key            | Value                                                                        |
|----------------|------------------------------------------------------------------------------|
| Challenge Name | LuffySeemsBroken                                                             |
| Author         | warlocksmurf                                                                 |
| Category       | Forensics                                                                    |
| Description    | Have you read One Piece? I heard Luffy has a new significant Gear coming up. |
| Challenge Type | Static                                                                       |
| Flag           | sunctf{lsb_and_pixels}                                                       |
| Score          | ???                                                                          |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

1) The flag is embedded within the LSB for the PNG image, just use tools like `zsteg` to extract it.

```
└─$ zsteg littleluffy.png 
b1,r,msb,xy         .. text: "0; HsTm="
b1,rgba,lsb,xy      .. text: "flag is sunctf{lsb_and_pixels}"
b3,r,msb,xy         .. text: "XS{xgrD#"
b3,g,msb,xy         .. text: "N|cLH8HG"
b3,bgr,lsb,xy       .. text: "%n7\tRY*M"
b3,rgba,lsb,xy      .. file: Atari 68xxx CPX file (version 06f6)
b4,r,lsb,xy         .. text: "b#\"E Gb%iDE&c4we35ED%SD"
b4,b,lsb,xy         .. text: "4fy0%T6fhvfh"
```

</details>
