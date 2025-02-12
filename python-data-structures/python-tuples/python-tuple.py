# PYTHON TUPLES

"""
-----------------------------
Python Data Structures: Tuples
-----------------------------
1. Python has 4 built-in data types used to store collections of data. This section will focus on "Tuples".
2. What is a Tuple? A "Tuple" is an ordered collection of items, similar to lists.
3. Tuples are "immutable," meaning their elements cannot be changed after the tuple is created.
This is a crucial distinction from lists.
4. Tuples are defined using parentheses ().
5. SYNTAX: tuple_name = ()  or tuple_name = (item1, item2, ...)
"""

# EXAMPLE 1: TUPLE HOLDING A COLLECTION OF FRUIT (OF TYPE STRING)
fruits = ("Orange", "Strawberry", "Apple", "Peach")
print(fruits)  # Expected Output: ('Orange', 'Strawberry', 'Apple', 'Peach')

# EXAMPLE 2: TUPLE HOLDING MIXED DATA TYPES
mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple) # Expected Output: (1, 'hello', 3.14, True)

# ------------------------------------------------------------------------------------------------------------------------------------- #

"""
----------------------
Tuple Characteristics
----------------------

1. Immutability:  As mentioned, tuples cannot be changed after creation.  You cannot add, remove, or modify items within a tuple.  
Attempting to do so will result in an error.
2. Ordered:  The items in a tuple maintain a specific order.  This order is preserved.
3. Indexing:  You can access individual items in a tuple using their index, just like lists.  Indexing starts at 0.
4. Common Tuple Operations:  While you can't modify a tuple directly, you can perform operations like:
    * Accessing elements (using indexing)
    * Slicing (creating a sub-section of the tuple)
    * Concatenation (combining tuples)
    * Finding the length of a tuple
"""

# EXAMPLE 3: Accessing Elements & Slicing
print(fruits[0])  # Expected Output: Orange
print(fruits[1:3]) # Expected Output: ('Strawberry', 'Apple')

# EXAMPLE 4: Concatenation
more_fruits = ("Mango", "Banana")
all_fruits = fruits + more_fruits
print(all_fruits) # Expected Output: ('Orange', 'Strawberry', 'Apple', 'Peach', 'Mango', 'Banana')

# EXAMPLE 5: Length of a Tuple
print(len(fruits)) # Expected Output: 4q
# ------------------------------------------------------------------------------------------------------------------------------------- #

