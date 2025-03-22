# Python Lamda functions

"""
1. In Python, functions are typically defined using the def keyword. However, for concise, one-time-use functions,
Python provides lambda functions, also known as anonymous functions.

2. A lambda function is a small, anonymous function that does not require a name and can have any number of arguments but only a
single expression. It is often used for short, simple operations where defining a full function using def would be unnecessary.

3. SYNTAX:
lambda parameters: expression

4. Storing a Lambda Function in a Variable
* Although lambda functions are anonymous, they can be assigned to a variable for reuse.
* f = lambda parameters: expression
"""

# Example: Adding 2 numbers
sum_of_numbers = lambda x,y: x + y
print(sum_of_numbers(4,5)) # Output: 9