# Lost Memories 1

| Key            | Value                                                                                                                                                                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Challenge Name | Lost Memories 1                                                                                                                                                                                                                                |
| Author         | warlocksmurf                                                                                                                                                                                                                                   |
| Category       | Forensics                                                                                                                                                                                                                                      |
| Description    | We managed to recover a memory dump from the compromised machine and require your analysis to obtain information about the attack. Can you identify when was the memory dump taken.<br><br>Flag format: `sunctf{2020-01-01 12:00:00+00:00}`. |
| Challenge Type | Static                                                                                                                                                                                                                                         |
| Flag           | sunctf{2024-09-10 13:58:14+00:00}                                                                                                                                                                                                              |
| Score          | ???                                                                                                                                                                                                                                            |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

```
└─$ vol -f memdump.raw windows.info     
Volatility 3 Framework 2.8.0
Progress:  100.00               PDB scanning finished                        
Variable        Value

Kernel Base     0xf80066a00000
DTB     0x1aa000
Symbols file:///home/kali/.local/lib/python3.11/site-packages/volatility3/symbols/windows/ntkrnlmp.pdb/D9424FC4861E47C10FAD1B35DEC6DCC8-1.json.xz
Is64Bit True
IsPAE   False
layer_name      0 WindowsIntel32e
memory_layer    1 FileLayer
KdVersionBlock  0xf8006760f400
Major/Minor     15.19041
MachineType     34404
KeNumberProcessors      2
SystemTime      2024-09-10 13:58:14+00:00
NtSystemRoot    C:\Windows
NtProductType   NtProductWinNt
NtMajorVersion  10
NtMinorVersion  0
PE MajorOperatingSystemVersion  10
PE MinorOperatingSystemVersion  0
PE Machine      34404
PE TimeDateStamp        Mon Dec  9 11:07:51 2019
```

</details>

# Lost Memories 2

| Key            | Value                                    |
|----------------|------------------------------------------|
| Challenge Name | Lost Memories 2                          |
| Author         | warlocksmurf                             |
| Category       | Forensics                                |
| Description    | What is the password of the system user? |
| Challenge Type | Static                                   |
| Flag           | sunctf{love_sunway}                      |
| Score          | ???                                      |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

```
└─$ vol -f memdump.raw windows.hashdump
Volatility 3 Framework 2.8.0
Progress:  100.00               PDB scanning finished                        
User    rid     lmhash  nthash

Administrator   500     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
Guest   501     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
DefaultAccount  503     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
WDAGUtilityAccount      504     aad3b435b51404eeaad3b435b51404ee        8a70cca3c9e0ee0b677d069e8b75ec79
warlocksmurf    1001    aad3b435b51404eeaad3b435b51404ee        e7edb365ce429af06ed3ddf783d9ba34
```

![sol1](/forensics_lost-memories/docs/sol1.png)

</details>

# Lost Memories 3

| Key            | Value                                                                                                                                                                                                       |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Challenge Name | Lost Memories 3                                                                                                                                                                                             |
| Author         | warlocksmurf                                                                                                                                                                                                |
| Category       | Forensics                                                                                                                                                                                                   |
| Description    | The victim accidentally executed a malicious executable in the system. What was the malicious executable called, its process ID and parent process ID?<br><br>Flag format: `sunctf{abc.exe_PID_PPID}`. |
| Challenge Type | Static                                                                                                                                                                                                      |
| Flag           | sunctf{inject0r.exe_5904_7780}                                                                                                                                                                              |
| Score          | ???                                                                                                                                                                                                         |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

```
└─$ vol -f memdump.raw windows.pstree  
Volatility 3 Framework 2.8.0
Progress:  100.00               PDB scanning finished                        
PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64   CreateTime      ExitTime        Audit   Cmd     Path

---SNIP---

*** 7780        4104    cmd.exe 0x868b83657080  2       -       1       False   2024-09-10 13:57:00.000000 UTC  N/A     \Device\HarddiskVolume2\Windows\System32\cmd.exe "C:\Windows\system32\cmd.exe"    C:\Windows\system32\cmd.exe
**** 7784       7780    conhost.exe     0x868b83763340  5       -       1       False   2024-09-10 13:57:00.000000 UTC  N/A     \Device\HarddiskVolume2\Windows\System32\conhost.exe      \??\C:\Windows\system32\conhost.exe 0x4 C:\Windows\system32\conhost.exe
**** 5904       7780    inject0r.exe    0x868b82d1e080  11      -       1       True    2024-09-10 13:57:41.000000 UTC  N/A     \Device\HarddiskVolume2\Users\warlocksmurf\Downloads\inject0r.exe inject0r.exe    C:\Users\warlocksmurf\Downloads\inject0r.exe
***** 6480      5904    notepad.exe     0x868b82db7300  4       -       1       True    2024-09-10 13:57:41.000000 UTC  N/A     \Device\HarddiskVolume2\Windows\SysWOW64\notepad.exe      "C:\Windows\System32\notepad.exe"       C:\Windows\SysWOW64\notepad.exe

---SNIP---
```

</details>

# Lost Memories 4

| Key            | Value                                                                                              |
|----------------|----------------------------------------------------------------------------------------------------|
| Challenge Name | Lost Memories 4                                                                                    |
| Author         | warlocksmurf                                                                                       |
| Category       | Forensics                                                                                          |
| Description    | The malicious executable injected the flag into its child process, can you retrieve the flag back? |
| Challenge Type | Static                                                                                             |
| Flag           | sunctf{v0latility_is_l0v3}                                                                         |
| Score          | ???                                                                                                |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

```
└─$ vol -f memdump.raw -o ~/Desktop windows.memmap --dump --pid 6480 
Volatility 3 Framework 2.8.0
Progress:  100.00               PDB scanning finished                        
Virtual Physical        Size    Offset in File  File output

0x8b0000        0xb776a000      0x1000  0x0     pid.6480.dmp
0x8b1000        0x9c1ed000      0x1000  0x1000  pid.6480.dmp
0x8b2000        0x10c586000     0x1000  0x2000  pid.6480.dmp
0x8b4000        0x382af000      0x1000  0x3000  pid.6480.dmp

---SNIP---
```

```
└─$ strings pid.6480.dmp | grep flag
The flag is here: c3VuY3Rme3YwbGF0aWxpdHlfaXNfbDB2M30=
flagsSelectW
?flags@ios_base@std@@QAEHH@Z
?flags@ios_base@std@@QBEHXZ
?resetiosflags@std@@YA?AU?$_Smanip@H@1@H@Z
?setiosflags@std@@YA?AU?$_Smanip@H@1@H@Z

---SNIP---
```

</details>

# Lost Memories 5

| Key            | Value                                                                                                                                                      |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Challenge Name | Lost Memories 5                                                                                                                                            |
| Author         | warlocksmurf                                                                                                                                               |
| Category       | Forensics                                                                                                                                                  |
| Description    | The victim kept his study notes somewhere in the machine. Can you recover his study notes and analyze it to make sure it is safe before handing it to him. |
| Challenge Type | Static                                                                                                                                                     |
| Flag           | sunctf{vba_macros_are_dangerous}                                                                                                                           |
| Score          | ???                                                                                                                                                        |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

*To make it less guessy, the study note file can be identified being executed by LibreOffice.

```
└─$ vol -f memdump.raw windows.pstree  
Volatility 3 Framework 2.8.0
Progress:  100.00               PDB scanning finished                        
PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64   CreateTime      ExitTime        Audit   Cmd     Path

---SNIP---

*** 820 4104    swriter.exe     0x868b81dcb080  2       -       1       False   2024-09-10 13:57:49.000000 UTC  N/A     \Device\HarddiskVolume2\Program Files\LibreOffice\program\swriter.exe     "C:\Program Files\LibreOffice\program\swriter.exe" -o "C:\Users\warlocksmurf\Documents\Study Notes\BSc (Hons) Information Technology (Computer Networking and Security) notes.doc"        C:\Program Files\LibreOffice\program\swriter.exe
**** 1704       820     soffice.exe     0x868b82de3080  2       -       1       False   2024-09-10 13:57:49.000000 UTC  N/A     \Device\HarddiskVolume2\Program Files\LibreOffice\program\soffice.exe     "C:\Program Files\LibreOffice\program\swriter.exe" -o "C:\Users\warlocksmurf\Documents\Study Notes\BSc (Hons) Information Technology (Computer Networking and Security) notes.doc" --writer       C:\Program Files\LibreOffice\program\soffice.exe
***** 1716      1704    soffice.bin     0x868b828602c0  18      -       1       False   2024-09-10 13:57:49.000000 UTC  N/A     \Device\HarddiskVolume2\Program Files\LibreOffice\program\soffice.bin     "C:\Program Files\LibreOffice\program\swriter.exe" "-o" "C:\Users\warlocksmurf\Documents\Study Notes\BSc (Hons) Information Technology (Computer Networking and Security) notes.doc" "--writer" "-env:OOO_CWD=2C:\\Users\\warlocksmurf\\Documents\\Study Notes"   C:\Program Files\LibreOffice\program\soffice.bin

---SNIP---
```

```
└─$ vol -f memdump.raw windows.filescan | grep BSc      
0x868b83b3b0d0.0\Users\warlocksmurf\Documents\Study Notes\BSc (Hons) Information Technology (Computer Networking and Security) notes.doc
0x868b8462c4c0  \Users\warlocksmurf\Documents\Study Notes\.~lock.BSc (Hons) Information Technology (Computer Networking and Security) notes.doc#
0x868b84639490  \Users\warlocksmurf\Documents\Study Notes\BSc (Hons) Information Technology (Computer Networking and Security) notes.doc
```

```
└─$ vol -f memdump.raw -o ~/Desktop windows.dumpfiles --virtaddr 0x868b84639490 
Volatility 3 Framework 2.8.0
Progress:  100.00               PDB scanning finished                        
Cache   FileObject      FileName        Result

DataSectionObject       0x868b84639490  BSc (Hons) Information Technology (Computer Networking and Security) notes.doc  Error dumping file
SharedCacheMap  0x868b84639490  BSc (Hons) Information Technology (Computer Networking and Security) notes.doc  file.0x868b84639490.0x868b828542a0.SharedCacheMap.BSc (Hons) Information Technology (Computer Networking and Security) notes.doc.vacb
```

```
└─$ olevba file.0x868b84639490.0x868b828542a0.SharedCacheMap.BSc\ \(Hons\)\ Information\ Technology\ \(Computer\ Networking\ and\ Security\)\ notes.doc.vacb 
olevba 0.60.2 on Python 2.7.18 - http://decalage.info/python/oletools
===============================================================================
FILE: file.0x868b84639490.0x868b828542a0.SharedCacheMap.BSc (Hons) Information Technology (Computer Networking and Security) notes.doc.vacb
Type: OLE
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls 
in file: file.0x868b84639490.0x868b828542a0.SharedCacheMap.BSc (Hons) Information Technology (Computer Networking and Security) notes.doc.vacb - OLE stream: u'Macros/VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
(empty macro)
-------------------------------------------------------------------------------
VBA MACRO NewMacros.bas 
in file: file.0x868b84639490.0x868b828542a0.SharedCacheMap.BSc (Hons) Information Technology (Computer Networking and Security) notes.doc.vacb - OLE stream: u'Macros/VBA/NewMacros'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Sub Sunway()
    Dim text As String
    Dim encodedFlag As String
    
    text = "Hello, World!"
    MsgBox "Original Text: " & text
    
    text = ReverseString(text)
    MsgBox "Reversed Text: " & text
    
    encodedFlag = "sun" & "ctf" & "{vba" & "_macros_" & "are_" & "dangerous}"
    MsgBox "Here is a hidden message: " & encodedFlag
    
End Sub

Function ReverseString(input As String) As String
    Dim i As Integer
    Dim output As String
    output = ""
    
    For i = Len(input) To 1 Step -1
        output = output & Mid(input, i, 1)
    Next i
    
    ReverseString = output
End Sub
```

</details>
