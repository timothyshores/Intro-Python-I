"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

import os
import sys

with open(os.path.join(sys.path[0], "foo.txt"), "r") as f:
    print(f.read())
    f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

fh = open("bar.txt", "w")
fh.write("Analytics deployment freemium sales gen-z iteration user experience network effects long tail holy grail.")
fh.write("Business plan backing responsive web design. ")
fh.write("Seed round influencer social media assets android low hanging fruit network effects stock gamification iPhone first mover advantage return on investment")
fh.close()

with open(os.path.join(sys.path[0], "bar.txt"), "r") as fh:
    print(fh.read())
    fh.close()
