The goal is, send a POST request to /flag

Take a URL input and show the website snapshot on submit (I am thinking of a more interesting context). Ban /flag request, unless from localhost. When request using GET method, ask explicitly for POST method (cauz the payload will be a lot more longer).

#1: Disallow localhost, 127.0.0.1, file:// etc. in input. Expect to use a bypass technique, e.g. hex ip addr.
#2: Use gopher:// to curate a POST request.