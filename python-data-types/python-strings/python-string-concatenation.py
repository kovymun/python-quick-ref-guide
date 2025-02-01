# Python String Concatenation

"""
---------------------------
Python String Concatenation
---------------------------

1. In simple terms, String concatenation is the process of joining two or more strings together to form a single string.
2. The basic method to execute string concatenation is to use the + operator.
3. + operator syntax: string_one + " " + string_two
4. Another option for string concatenation is to use formatted strings, but this will be discussed in the file named
"python-formatted-strings.py"

"""


first_name = "Calvin"
last_name = "Harris"
full_name = first_name + " " + last_name
print(full_name)  # Expected Output: "Calvin Harris"

# Using the Join() method

words = ["Hello", "World"]
result = " ".join(words)
print(result)
