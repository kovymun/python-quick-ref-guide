# PYTHON LIST METHODS

"""
-------------------
Python List Methods
-------------------

1. A list method is a built-in function that allows you to perform different/various actions on a list in Python.
2. For example, list methods allow you to change, organize, or retrieve information from a list. Example: Adding, removing or sorting
items in a list.
3. Some of the most common list methods are: append(), extend(), pop(), remove(), and sort().

METHODS:
* append(): SYNTAX: list.append(element). The append() method adds an item x to the end of the list.
* pop(): SYNTAX: list.pop(index-position). The pop() method removes a list element at the specified position. It is also important to note is that pop() does two things at once — it modifies the original list and returns the removed value.
If no index is provided, the last element of the list is removed and returned by default. This method also modifies the original list.
* copy(): SYNTAX: list.copy(). The copy() method returns a copy of the specified list.

"""

# EXAMPLE: LIST APPEND METHOD
# The append() method adds an item x to the end of the list. In this example, we are adding the "cart item: apple" to the "cart" list.
cart = ["pears", "cactus"]
cart.append("apple")

print(cart)  # Output: ['pears', 'cactus', 'apple']

# Example: LIST COPY METHOD

students = ["Tanya", "Giselle", "Esme"]
student_copy = students.copy()
print(student_copy)  # Output: ['Tanya', 'Giselle', 'Esme']
