"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading.
# Print all the contents of the file, then close the file.

with open("foo.txt", "r") as f:
    file_content = f.read()
    print(file_content)

# Check that f has been closed.

print(f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open("bar.txt", "w") as b:
    b.write("My name is Taylor.\n")
    b.write("This file is part of Assignment 1.\n")
    b.write("You're most likely reading this on GitHub.")

# Check that file has been closed.

print(b.closed)

# Check the contents of the file just written.

with open("bar.txt", "r") as c:
    print(c.read())

# Check that file has been closed.

print(c.closed)