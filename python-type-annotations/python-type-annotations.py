# Python Type Annotations

"""
Python is traditionally a dynamically typed programming language, meaning variable types are determined at runtime.
However, Python provides type annotations (also known as "type hints") to improve code readability and help static analysis tools
catch potential errors before execution.

Why Use Type Annotations?
* Improves code clarity and maintainability
* Makes collaboration easier by showing expected input/output types

BASIC SYNTAX:
variable_name: data_type = value

Examples using Type Annotations
name: str = "Alice"  # 'name' is expected to be a string
age: int = 25        # 'age' is expected to be an integer
height: float = 1.75 # 'height' is expected to be a float




"""

# TEST EXAMPLES
name: str = "John"  # 'name' is expected to be a string
age: int = 30       # 'age' is expected to be an integer

print(f"Hello, my name is {name}, and I am {age} years old") # Output: Hello, my name is John, and I am 30 years old

def greeting(n: str) -> str:  # 'n' for name is a string, and the function returns a string
    return f"Hello, {n}!"

print(greeting("Sally")) # Output: Hello, Sally!






