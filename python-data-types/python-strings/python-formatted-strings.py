# PYTHON FORMATTED STRINGS

"""
------------------------
Python Formatted Strings
------------------------
1. In Python, "formatted strings" allow you to embed expressions inside string literals, using placeholders
or formatting syntax. This makes it easier to create dynamic strings without manually concatenating values.

2. f-strings, or formatted string literals, were introduced in Python 3.6 and are the most concise and preferred
way to format strings in modern Python.
* f-strings start with the letter "f" before the string.
* Expressions inside curly braces "{}" are evaluated and inserted into the string.

3. SYNTAX: formatted_string = f"some text {expression}"
EXAMPLE: introduction = f"My name is {name} and I am {age} years old."
"""
from statistics import quantiles

# Example: Formatted String Literals (f-strings)

# Defining variables
fruit = "apple"
fruit_price = 33

# Using f-string to embed variables directly into the string
formatted_string = f"The cost of a single {fruit} is R{fruit_price}."

# Print the formatted string
print(formatted_string) #Output: The cost of a single apple is R33

# Example: Formatted String Literals - with expressions inside f-strings
# Defining Variables
cart_item = "Chocolate"
cart_item_price = 22
quantity = 3

# Using f-string to embed variables and perform an expression inside the string
formatted_string = f"The cost of {quantity} {cart_item}s is ${cart_item_price * quantity}."

# Print the formatted string
print(formatted_string)  # Output: The cost of 3 Chocolates is $66.



