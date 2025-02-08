# PYTHON DICTIONARIES: METHODS

"""
------------------------------------
Python Data Structures: Dictionaries - Methods
------------------------------------
1. This section expands on dictionaries, focusing on commonly used methods.
"""

# EXAMPLE: DICTIONARY HOLDING THE RELATED DETAILS OF A PERSON

person = {
    "name": "Alice",
    "age": 28,
    "city": "Tokyo",
}

print(person)  # Output: {'name': 'Alice', 'age': 28, 'city': 'Tokyo'}

# 1. Accessing Items:

# Accessing a value by its key:
name = person["name"]
print(name)  # Output: Alice

# Using .get() method (safer, returns None if key doesn't exist):
age = person.get("age")
print(age)  # Output: 28

# Using .get() with a default value if the key is not found:
country = person.get("country", "Unknown") # Key 'country' doesn't exist
print(country)  # Output: Unknown


# 2. Adding/Updating Items:

# Adding a new key-value pair:
person["occupation"] = "Software Engineer"
print(person)  # Output: {'name': 'Alice', 'age': 28, 'city': 'Tokyo', 'occupation': 'Software Engineer'}

# Updating an existing value:
person["age"] = 29
print(person)  # Output: {'name': 'Alice', 'age': 29, 'city': 'Tokyo', 'occupation': 'Software Engineer'}


# 3. Removing Items:

# Removing an item using del:
del person["city"]
print(person)  # Output: {'name': 'Alice', 'age': 29, 'occupation': 'Software Engineer'}

# Removing an item using .pop() (returns the removed value):
occupation = person.pop("occupation")
print(person)  # Output: {'name': 'Alice', 'age': 29}
print(occupation) # Output: Software Engineer

# Removing the last inserted item using .popitem() (returns the removed key-value pair as a tuple):
item = person.popitem()
print(person) # Output: {'name': 'Alice'}
print(item) # Output: ('age', 29)


# 4. Checking for Keys:

# Using the 'in' keyword:
has_name = "name" in person
print(has_name)  # Output: True

has_city = "city" in person
print(has_city)  # Output: False


# 5. Dictionary Views:

# .keys(): Returns a view object containing the keys:
keys = person.keys()
print(keys)  # Output: dict_keys(['name'])

# .values(): Returns a view object containing the values:
values = person.values()
print(values)  # Output: dict_values(['Alice'])

# .items(): Returns a view object containing the key-value pairs (as tuples):
items = person.items()
print(items)  # Output: dict_items([('name', 'Alice')])

# 6. Copying a Dictionary:

# Using .copy() to create a shallow copy:
person_copy = person.copy()
print(person_copy) # Output: {'name': 'Alice'}

# 7. Clearing a Dictionary:

# Using .clear() to remove all items:
person.clear()
print(person)  # Output: {}

# 8. Updating one dictionary with another
other_person = {"city": "New York", "country": "USA"}
person_copy.update(other_person)
print(person_copy) # Output: {'name': 'Alice', 'city': 'New York', 'country': 'USA'}