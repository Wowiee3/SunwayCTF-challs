Description: I protected my environment keys and prevented arbitary file read from sunway hackers!

Deployment: 
1) Build and run the dockerfile, the server will be listening on port 5001.
2) Distirbute schools.zip to the participants as it is a whitebox challenge.
3) solve.py can be used to check the challenge is working as intended (it will solve the challenge and get the flag), change the URL to the remote instance to mimic a participant.

Solve: 
1) Each program running would have their corresponding process id (PID), use this behaviour to read the environment file with /proc/1/environ as /proc/self/environ is blocked.
2) The path filtering on "../" is done non-recursively, and can be bypassed with examples such as "....//" or "..././" sequence as it will be stripped to "../".
3) Now we can read arbitary files by going up directories with the "../" sequence.
4) An example valid filepath to read the environment variable for flag "/file?school=....//....//proc/1/environ".



