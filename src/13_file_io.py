"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

# Change working directory
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(r"foo.txt") as f:
    for line in f:
        print(line, end="")

    # Close file
    f.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

famous_lines = [
    "Hello, world!\n",
    "The quick brown fox jumps over the lazy dog\n",
    "Lions and tigers and bears, oh my!\n",
]

with open(r"bar.txt", "r") as f:
    for line in famous_lines:
        f.write(line)

    f.close()
