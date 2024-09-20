Description: Admins tried to disable my money glitch but I still found a way.

Deployment: 
1) Build and run the dockerfile, the server will be listening on port 5003.
2) Distribute shopping.zip to the participants as it is a whitebox challenge.
3) solve.py can be used to check the challenge is working as intended (it will solve the challenge and get the flag), change the URL to the remote instance to mimic a participant.

Solve: 
1) The challenge is an Server Side Request Forgery (SSRF) & business logic challenge.
2) SSRF is required to hit the registration endpoint as only localhost is allowed. While the path sent is /admin in the frontend, we can change this to /register with tools like burp.
3) Change "/admin" path to something like "username=a&password=b&path=/register?username=shen%26password=shen" to register a user. (%26 -> &)
4) Each user only has 50 currency which is not enough to buy the flag because it has a price of 100.
5) Buy a negative amount of mugs to increase your account balance as the logic does not check if the item quantity is a negative, i.e. -5 mugs to get extra 50 currency.
6) Buy the flag.



