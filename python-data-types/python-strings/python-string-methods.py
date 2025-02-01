greeting = "hello learner"


print(greeting.upper())    # Expected Output: "HELLO WORLD"
print(greeting.lower())    # Expected Output: "hello world"
print(greeting.replace("learner", "beyonce"))  # Expected Output: "hello beyonce"

# ------------------------------------------------------------------------------------------------------------------------------------- #
"""
-------------
Split method: 
-------------
1. The split() method in Python is used to split a string into a LIST of substrings based on a specified delimiter (or seperator).
2. Examples of delimiters/seperators: comma(",") |  space (" ") | hyphen ("-") | pipe ("|")
3. By default, it splits on whitespace (spaces, tabs, or newlines).
4. SYNTAX: string.split(separator, maxsplit)
   * maxsplit: Specifies how many splits (or separations) to do. Default value = -1
"""

# Example using the split() method
greeting_sep = greeting.split() # default split (whitespaces)
print(greeting_sep) # Expected Output: ['hello', 'learner']

# ------------------------------------------------------------------------------------------------------------------------------------- #