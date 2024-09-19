Description: My security friend said my uni ping project has Remote Code Execution???

Deployment: 
1) Build and run the dockerfile, the server will be listening on port 5004.
2) Distribute ping.zip to participants as it is a whitebox challenge.
3) solve.py can be used to check the challenge is working as intended (it will solve the challenge and get the flag), change the URL to the remote instance to mimic a participant.

Solve: 
1) Supply an IP such as 
2) Generate a valid cookie with boolean true in price property to bypass the price check.
3) Send a GET request to /price.php to obtain the flag due to PHP loose comparison, == instead of ===.
4) Command injection in IP address due to IPv6 parsing. [https://docs.python.org/3/library/ipaddress.html](https://docs.python.org/3/library/ipaddress.html#:~:text=zone)


