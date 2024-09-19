Description: Yet another robots web challenge.

Deployment: 
1) Build and run the dockerfile, the server will be listening on port 5000.
2) No files to be distributed as it is a blackbox challenge (classic robots.txt challenge)
3) solve.py can be used to check the challenge is working as intended (it will solve the challenge and get the flag), change the URL to the remote instance to mimic a participant.

Solve: 
1) Go to /robots.txt to discover /codeGen.php and /flag.php
2) /codeGen.php has a random number function which has a fixed seed. This produces the same number everytime, copy the code and execute it to obtain the number.
3) Input the number at flag.php to get the flag.


