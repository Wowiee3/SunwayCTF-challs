## MasterFanumTax
Mr Fanum might have accidentally placed his secret code in a text file on the Documents folder, can you recover it?

Flag: `sunctf{b4s1cs_0f_mft}`

Intended solution: Parse and analyze the MFT for txt files, and carve the file content using its offset.
Unintended solution: Strings the MFT for the encoded flag.
