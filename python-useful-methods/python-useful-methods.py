# PYTHON USEFUL METHODS

"""
---------------------
Python Useful Methods
---------------------
1. range(): The range() function creates a sequence of numbers, often used in loops.
2. len(): The len() function returns the number of items in a data type/structure (like a list or string).
3. sum(): The sum() function adds all elements in an iterable.
4. count(): The count() method returns the number of times a specified value occurs in a string or list.
"""

# EXAMPLE USING SUM() METHOD

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15

# EXAMPLE USING COUNT() METHOD

python_greeting = "hello world"
count_of_l = python_greeting.count("l")
print(count_of_l)  # Output: 3

nums = [1, 2, 2, 3, 2, 4, 2]
count_of_2 = nums.count(2)
print(count_of_2)  # Output: 4

count_of_5 = nums.count(5)
print(count_of_5) # Output: 0