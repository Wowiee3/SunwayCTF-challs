# MasterFanumTax

| Key            | Value                                                                                |
|----------------|--------------------------------------------------------------------------------------|
| Challenge Name | MasterFanumTax                                                                       |
| Author         | warlocksmurf                                                                         |
| Category       | Forensics                                                                            |
| Description    | A secret code was stored in a text file on the Documents folder, can you recover it using only the MFT? |
| Challenge Type | Static                                                                               |
| Flag           | sunctf{b4s1cs_0f_mft}                                                                |
| Score          | ???                                                                                  |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

Intended solution: Parse and analyze the MFT for .txt files in Documents folder, and carve the flag file using its offset.

```
➜ .\MFTECmd.exe -f 'C:\Users\ooiro\Documents\shared\Created Challlenges\SunwayCTF2024\Forensics\[easy] MasterFanumTax\$MFT' --de 114099
MFTECmd version 1.2.2.1

Author: Eric Zimmerman (saericzimmerman@gmail.com)
https://github.com/EricZimmerman/MFTECmd

Command line: -f C:\Users\ooiro\Documents\shared\Created Challlenges\SunwayCTF2024\Forensics\[easy] MasterFanumTax\$MFT --de 114099

Warning: Administrator privileges not found!

File type: Mft

Processed C:\Users\ooiro\Documents\shared\Created Challlenges\SunwayCTF2024\Forensics\[easy] MasterFanumTax\$MFT in 1.2572 seconds

C:\Users\ooiro\Documents\shared\Created Challlenges\SunwayCTF2024\Forensics\[easy] MasterFanumTax\$MFT: FILE records found: 114,161 (Free records: 6,614) File size: 118MB


Dumping details for file record with key 0001BDB3-00000004

Entry-seq #: 0x1BDB3-0x4, Offset: 0x6F6CC00, Flags: InUse, Log seq #: 0x162C7C19, Base Record entry-seq: 0x0-0x0
Reference count: 0x1, FixUp Data Expected: 05-00, FixUp Data Actual: 00-00 | 00-00 (FixUp OK: True)

**** STANDARD INFO ****
  Attribute #: 0x0, Size: 0x60, Content size: 0x48, Name size: 0x0, ContentOffset 0x18. Resident: True
  Flags: Archive, Max Version: 0x0, Flags 2: None, Class Id: 0x0, Owner Id: 0x0, Security Id: 0x751, Quota charged: 0x0, Update sequence #: 0x1AAFA28

  Created On:         2024-09-08 09:45:24.4321235
  Modified On:        2024-09-08 09:46:16.6508734
  Record Modified On: 2024-09-08 09:46:16.6508734
  Last Accessed On:   2024-09-08 09:46:17.6821033

**** FILE NAME ****
  Attribute #: 0x4, Size: 0x70, Content size: 0x52, Name size: 0x0, ContentOffset 0x18. Resident: True

  File name: flag.txt
  Flags: Archive, Name Type: DosWindows, Reparse Value: 0x0, Physical Size: 0x0, Logical Size: 0x0
  Parent Entry-seq #: 0xCCD2-0x3

  Created On:         2024-09-08 09:45:24.4321235
  Modified On:        2024-09-08 09:45:24.4321235
  Record Modified On: 2024-09-08 09:45:24.4321235
  Last Accessed On:   2024-09-08 09:45:24.4321235

**** OBJECT ID ****
  Attribute #: 0x5, Size: 0x28, Content size: 0x10, Name size: 0x0, ContentOffset 0x18. Resident: True

  Object Id:            82e9222e-6dc5-11ef-a309-000c29accac9
    Object Id MAC:        00:0c:29:ac:ca:c9
    Object Id Created On: 2024-09-08 09:34:14.4076334

  Birth Volume Id:      00000000-0000-0000-0000-000000000000

  Birth Object Id:      00000000-0000-0000-0000-000000000000
  Domain Id:            00000000-0000-0000-0000-000000000000

**** DATA ****
  Attribute #: 0x1, Size: 0x78, Content size: 0x5B, Name size: 0x0, ContentOffset 0x18. Resident: True

  Resident Data

  Data: 48-65-72-65-20-69-73-20-74-68-65-20-73-65-63-72-65-74-20-68-65-78-20-63-6F-64-65-3A-20-37-33-20-37-35-20-36-65-20-36-33-20-37-34-20-36-36-20-37-62-20-36-32-20-33-34-20-37-33-20-33-31-20-36-33-20-37-33-20-35-66-20-33-30-20-36-36-20-35-66-20-36-64-20-36-36-20-37-34-20-37-64

    ASCII:   Here is the secret hex code: 73 75 6e 63 74 66 7b 62 34 73 31 63 73 5f 30 66 5f 6d 66 74 7d
    UNICODE: ???????????????"?????????????????"??%?????"???
```

Unintended solution: Strings the MFT for the encoded flag.

</details>
