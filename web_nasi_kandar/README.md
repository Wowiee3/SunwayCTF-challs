Description: Yet another robots web challenge.

Deployment: 
1) Build and run the dockerfile, the server will be listening on port 5000.
2) No files should be given to the user as it is a blackbox style challenge (classic robots.txt challenge).
3) solve.py can be used to check the challenge is working as intended (it will solve the challenge and get the flag), change the URL to the remote instance to mimic a participant.

Solve: 
1) Go to /robots.txt to find /flag.php and /codeGen.php.
2) Random function is given with seed in /codeGen.php, which generates the same number everytime.
3) Copy and execute the code to get the random number.
4) Go to /flag.php and input the number for the flag.


