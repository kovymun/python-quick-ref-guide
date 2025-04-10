# Python For-loops
"""
What is a For Loop?

* In Python, a "for loop" is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) and execute a
block of code for each item in that sequence. It is especially useful when you know ahead of time how many times you want to loop.
* Think of it as a way to "automatically repeat tasks" without manually writing code multiple times.

BASIC SYNTAX:
-------------
for variable in data_structure:
    # Code logic to execute
"""

# Example 1: This loop prints each item from the list "fruits" one by one
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry

# -------------------------------------------------- Using the Range Function ----------------------------------------------------------
# The "range()" function generates a sequence of numbers.
# It's commonly used with for loops when you want to iterate a specific number of times.

"""
SYNTAX:
for variable in range(start, stop, step):
    # Code logic
"""

# Example 2:
for num in range(1, 6):  # Loops from 1 to 5 (6 is excluded)
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# Example 3 (with step):
for num in range(0, 10, 2):
    print(num)

# Output:
# 0
# 2
# 4
# 6
# 8

# -------------------------------------------------- Looping Through Strings -----------------------------------------------------------
# A string is a sequence of characters, so you can loop through it character by character.

# Example
for letter in "Python":
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n

# ----------------------------------------------- Looping Through Dictionaries -------------------------------------------------------
# You can loop through the keys, values, or both in a dictionary.

# Example 5:
student = {"name": "Alice", "age": 25}

for key, value in student.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 25



# ----------------------------------------------- The break and continue Statements --------------------------------------------------
# `break` stops the loop completely.
# `continue` skips the current iteration and moves to the next one.

# Example (break):
for num in range(1, 10):
    if num == 5:
        break
    print(num)

# Output:
# 1
# 2
# 3
# 4

# Example (continue)
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# Output:
# 1
# 2
# 4
# 5

# -----------------------------------------------  Using else with a for loop ---------------------------------------------------------
# The `else` block after a `for` loop runs only if the loop **was not terminated by break**.

# Example:
for num in range(3):
    print(num)
else:
    print("Loop completed successfully.")

# Output:
# 0
# 1
# 2
# Loop completed successfully.

# ------------------------------------------------ Looping with enumerate() ----------------------------------------------------------
# The `enumerate()` function lets you loop over something and have an automatic counter.

# Example
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")

# Output:
# 0: Alice
# 1: Bob
# 2: Charlie

"""
--------
SUMMARY:
--------
- Use `for` loops to iterate over sequences like lists, tuples, strings, dictionaries, or ranges.
- Combine `range()`, `enumerate()`, and `dictionary.items()` for more powerful loops.
- Use `break` and `continue` to control loop flow.
- Optional `else` block runs only if the loop completes without interruption.
"""

