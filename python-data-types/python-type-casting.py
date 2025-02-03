#PYTHON DATA TYPE CASTING

"""
-------------------
Python Type Casting
-------------------
1. What is Type Casting? Type casting (also known as type conversion) is the process of converting one data type into another.
Python supports two types of type conversion:
* Implicit Type Casting – Done automatically by Python.
* Explicit Type Casting – Done manually by using built-in functions.
* Common Type Casting Functions: int(x) | float(x) | str(x) | bool(x) | list(x) | tuple(x) | set(x).
"""

# Example: Explicit Type Casting (Converting a string to an integer)
# Define a variable with a numeric value stored as a string
numberText = "12"

# Print the type of numberText before conversion
print(type(numberText))  # Output: <class 'str'> (string)

# Convert the string to an integer using the int() function
number = int(numberText)

# Print the converted value
print(number)  # Output: 12

# Print the type of number after conversion
print(type(number))  # Output: <class 'int'> (integer)

# Example: Converting an integer to a boolean

age = 32  # A non-zero integer

is_age_truthy = bool(age)  # Convert to boolean

print(is_age_truthy)  # Output: True (since non-zero values are truthy)
