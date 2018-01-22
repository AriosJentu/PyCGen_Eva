# Python Crypt Generator
Simple Python Code Crypt Generator (for protection your own projects)
With this scripts you can make your project protection. Here you can find functions for getting request code, with this request code you can generate activation code, and then with comparing function you can check, is activation code valid, or not. Very simple algorythm, what I've generated for 1-2 hours.


This files generates from basic templates custom files. 
Differences between pairs of files, what you can generate are in string of randomized available chars for crypting (alphabet), in hash-string, what generating with script, and in random shifting count of alphabet string.
This script generates two files:
- "server.py" has functions for end-user application
- "activation.py" has functions for administrators, where he can generate activation code by request code of user. 

There are 3 basic functions:
- str get_request() - creating for user random request code, using hash-string
- str/bool get_activation(str request) - creating by request code - activation code (False when can't create activation code by reques)
- bool check_activation_code(str request, str activation) - checking sums of request code and activation code, and returns true, if activation code is valid
 
How to use:
1) Execute in command shell with python file generator.py
2) Select option what you want

Thats all
