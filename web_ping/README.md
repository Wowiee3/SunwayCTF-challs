Description: My security friend said my uni ping project has Remote Code Execution???

Deployment: 
1) Build and run the dockerfile, the server will be listening on port 5004.
2) Distribute ping.zip to participants as it is a whitebox challenge.
3) solve.py can be used to check the challenge is working as intended (it will solve the challenge and get the flag), change the URL to the remote instance to mimic a participant.

Solve: 
1) Command injection in user_supplied_IP due to IPv6 zone parsing [https://docs.python.org/3/library/ipaddress.html](https://docs.python.org/3/library/ipaddress.html#:~:text=zone).
2) Supply a valid IPv6 address such as ::1%;cat flag.txt;
3) Obtain flag.


