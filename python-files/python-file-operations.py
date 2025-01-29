# PYTHON FILES AND FILE OPERATIONS

"""
----------------
Python Files and File operations

1. Python allows you to read, write, and manipulate files easily.
2. File types supported in Python: .txt | .json | .csv | .jpg | mp4
3. Before you read or write to a file, you must open it using the open() function.

SYNTAX: file = open("filename", "mode")
* "filename" : The name of the file with extension.
* "mode": Specifies what you want to do with the file.
* File modes:
"r" : read file
"r+" : read and write file
"w" : write file. Creates a new file if it doesn’t exist or overwrites the existing file.
"a" : append to file. Adds content to an existing file.

4. FILE OPERATIONS EXAMPLE:

file = open("file.txt", "r")  # Open in read mode
content = file.read()  # Read the whole file
print(content)
file.close()  # Close the file

"""

