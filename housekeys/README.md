## House Keys
Dr House encrypted the flag with his public key, but he accidentally left his private key on the table.

Flag: `sunctf{d0ct0r_h0us3_l0st_h1s_k3ys}`

Decrypt the encrypted flag with the private key given: `openssl rsautl -decrypt -inkey private_key.pem -in flag.txt.enc -out flag.txt`
