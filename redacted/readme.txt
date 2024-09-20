title: Redacted
category: web
desc: The solution to this challenge is: Read the `flag` by <REDACTED - this has violated our community guidelines.>
author: wolfishLamb

flag: sunctf{wh0_c4m3_up_w17h_7h15_8r1ll14n7_f347ur3}

solution:
The key to this challenge is RegEx. In older PHP versions (<5.5), there is an `e` modifier that allows you to use PHP
code within the RegEx. Something like `file_get_contents("flag")` will allow you to read any file on the server.
