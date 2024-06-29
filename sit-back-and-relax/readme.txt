title: Sit Back and Relax
category: misc
desc: Feeling tired after all those challenges? Take a break and have some coffee! Request the server to brew some
      coffee, probably it will dispense you the flag.
author: wolfishLamb

flag: sunctf{n3v3r_8r3W_c0ff33_1n_4_734p07}

solution: curl --request BREW <the_server_url>
explanation: This challenge is a reference to the HTTP method `BREW`. The `BREW` method is not a standard HTTP method,
             but it is defined in RFC 2324 as an April Fools' joke.

             The challenge description hints that the server will dispense the flag if you "request" it to "brew" some
             coffee. Besides, the image that shows a teapot is actually from the setup of error418.net.

             To solve the challenge, you can send a `BREW` request to the server using `curl` or any similar tools. The
             flag will be returned in the response.

             On the Wikipedia page for HTCPCP, you can find the `BREW` method, which asks the server to brew coffee. It
             also mentions that `POST` can be used for this purpose, but it is deprecated. If this challenge were to be
             made easier, we could let the server respond to a `POST` request as well.
