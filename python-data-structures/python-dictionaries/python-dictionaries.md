## PYTHON DICTIONARIES

### Python Data Structures: Dictionaries

1. Python has 4 built-in data types used to store collections of data. This section will focus on "Dictionaries".
2. What is a Dictionary? A "Dictionary" is a collection of key-value pairs, where each key is unique. (Similar to an
   object in JavaScript)
3. The dictionary items are unordered and mutable.
4. Defined using curly braces {}.
5. SYNTAX:

```
dictionary_name = {
    key1: value1,
    key2: value2,
}
```

### EXAMPLE: DICTIONARY HOLDING THE RELATED DETAILS OF A PERSON

```
person = {
"name": "Alice",
"age": 28,
"city": "Tokyo",
}

print(person) #Output: {'name': 'Alice', 'age': 28, 'city': 'Tokyo'}
```

---

### Iterating through a Dictionary

**1. Iterating over Dictionary Keys:**

- When you loop through a dictionary directly, you iterate over its keys by default.

```
SYNTAX:
for key in my_dict:
    print(key)

# Alternative using the .keys() method (explicit, but less common in modern Python):
for key in my_dict.keys():
    print(key)
    
EXAMPLE: 
person = {
"name": "Alice",
"age": 28,
"city": "Tokyo",
}

for key in person:
   print(key, end=" ") #Output: name age city 
```

**2. Iterating over Dictionary Values:**

- Use the .values() method to loop through only the values.

```
SYNTAX:
for value in my_dict.values():
  print(value)
  
EXAMPLE:
my_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}

for value in my_dict.values():
    print(value, end=" ") # OUTPUT: 1 2 3
```

**3. Iterating Over Both Keys and Values:**

- The most common and Pythonic way to access both keys and values is using the .items() method, which returns key-value
  pairs as tuples that can be unpacked directly in the for loop.

```
SYNTAX: 
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
    
EXAMPLE:
my_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}

# OUTPUT: 
Key: apple, Value: 1
Key: banana, Value: 2
Key: cherry, Value: 3

```
  



