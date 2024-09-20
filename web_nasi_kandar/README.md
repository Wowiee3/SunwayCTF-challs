Description: Guess the price of your nasi kandar to win a flag.

Deployment: 
1) Build and run the dockerfile, the server will be listening on port 5002.
2) Distribute nasi_kandar.zip to participants as it is a whitebox challenge.
3) solve.py can be used to check the challenge is working as intended (it will solve the challenge and get the flag), change the URL to the remote instance to mimic a participant.

Solve: 
1) Login with "Admin" or any variation due to case-insensitive nature of MySQL.
2) Generate a valid cookie with boolean true in price property to bypass the price check.
3) Send a GET request to /price.php to obtain the flag due to PHP loose comparison, == instead of ===.
4) An integer when compared to boolean true with == is always true, as the type is not enforced (https://www.php.net/manual/en/types.comparisons.php).


