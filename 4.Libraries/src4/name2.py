# Adds error checking

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too much arguments")
else:
    print("hello, my name is", sys.argv[1])