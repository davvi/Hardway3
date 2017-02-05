# Hardway3
Zed A Shaws python the Hardway. In the interest of challenging myself. I shall port all lessons to python 3.
As an engineer I will make some small changes out side of the general syntax change for porting.
I will usually always declare the interpreter to run. So all you need to do is add the executable bit to the script and you can run it as ./ex2.py etc.

If I have a daft typo in the code let us know.

If you are Zed Shaw. Thank you. If you are not go to his site and support his awesome work http://learnpythonthehardway.org/book

Excerise notes!

ex1.py

And for the rest of the work, you'll notice the change to the print statement. It is now a proper function with proper syntax.

ex11.py

raw_input is now just input. I've made some obvious changes just to the strings, I'm Australian, Metric is awesome.. Live with it.. or just change it to make sense for you.

ex25.py

Note that this one doesn't start with #!/usr/bin/env python.. after completing the exersise listed on Zed's website, try to learn why I've not done this.

ex26.py

This file has been ported to python 3 .. However I have left Zed's errors in there as intended for this excersize.. Please go through and fix the errors. 

ex41.py

This one took a bit of work .. There where few changes to the standard library organisation in python 3.
from urllib import urlopen is no from urllib.request import urlopen
The file that we pull from the website is all ascii .. to make this properly work we decode this to utf-8.
other then that .. there are the usual changes here.
