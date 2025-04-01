# Python Regular expressions (Regex)
"""
The re module in Python provides support for regular expressions (regex), which are patterns used to match, search, and manipulate text.
It is commonly used for tasks like data validation, text parsing, and string manipulation.

"""
import re  # Importing the 're' module, which provides support for working with regular expressions.

# Define a string to search within
text = "Python is amazing!"

# Use the re.search() function to look for the word "Python" in the text.
# The 'r' before the string (r"Python") denotes a raw string, which is useful for regex patterns.
match = re.search(r"Python", text)

# Check if a match was found
if match:
    # If a match is found, print the matched text using match.group()
    # The .group() method retrieves the exact substring that was matched.
    print("Match found:", match.group())  # Output: Match found: Python

