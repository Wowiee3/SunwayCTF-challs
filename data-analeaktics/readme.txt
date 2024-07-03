title: Data Analeaktics
category: web
desc: Exploring a massive dataset can be a headache. With our powerful web application, SunQuery, you will be able to filter and search for data with ease.
author: wolfishLamb

flag: sunctf{wh0_c4m3_up_w17h_7h15_8r1ll14n7_f347ur3}

solution:
The key to this challenge is regex. In older PHP versions (<5.5), there is an `e` modifier which allows you to use PHP code within the regex. Something like `eval('cat /flag.txt')` will allow RCE.



---< will implement this later >---
Data is read from a file.