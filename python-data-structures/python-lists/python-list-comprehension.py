# PYTHON LIST COMPREHENSION

# List comprehensions in Python share conceptual similarities with JavaScript's map and filter functions.

# Basic Syntax:
# new_list = [expression for item in iterable]
# With Conditional: new_list = [expression for item in iterable if condition]
"""
1. expression: The operation performed on each item.
2. item: A variable representing each element in the iterable.
3. iterable: The source of data (e.g., list, tuple, string, range).
4. condition: An optional filter that determines which items are included.
"""

numbers = list(range(0, 8))
print(numbers) # Output: [0, 1, 2, 3, 4]

# Example: Squaring numbers
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers) # Output: [0, 1, 4, 9, 16]

# Example: Even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers) # Output: [0, 2, 4]