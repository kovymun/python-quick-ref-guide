"""
=================
PYTHON DECORATORS
=================

--------------------
What are decorators?
--------------------
Decorators are like gift wrappers for your functions.
They add extra functionality without changing the original function's code.

Think of it like this:
- You have a sandwich (your function)
- You wrap it in foil (the decorator)
- The sandwich stays the same, but now it's wrapped and easier to handle

-------------------
Why use decorators?
-------------------
- Keep your code DRY (Don't Repeat Yourself)
- Add functionality like logging, timing, or authentication
- Make code cleaner and more readable
- Separate concerns (what a function does vs. how it behaves)

==========
THE BASICS
==========
"""


# 1. FUNCTIONS ARE FIRST-CLASS CITIZENS
# In Python, functions can be passed around like any other variable

def greet():
    return "Hello!"


# You can assign functions to variables
say_hello = greet
print(say_hello())  # Output: Hello!


# 2. FUNCTIONS INSIDE FUNCTIONS
# You can define functions inside other functions

def outer():
    message = "I'm from outer function"

    def inner():
        return message

    return inner


my_func = outer()
print(my_func())  # Output: I'm from outer function


# 3. FIRST DECORATOR
# A decorator is just a function that takes a function and returns a new function

def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")

    return wrapper


def say_whee():
    print("Whee!")


# Manual decoration
say_whee = my_decorator(say_whee)
say_whee()


# 4. THE @ SYNTAX (Syntactic Sugar)
# Python gives us a cleaner way to apply decorators

def my_decorator(func):
    def wrapper():
        print("Before!")
        func()
        print("After!")

    return wrapper


@my_decorator  # This is the same as: say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")


say_hello()

"""
===================
REAL-WORLD EXAMPLES
===================
"""

# 5. TIMING DECORATOR
# Measure how long a function takes to run
# Like using a stopwatch for your code

import time


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Function took {end - start:.4f} seconds")

    return wrapper


@timer
def slow_function():
    time.sleep(1)
    print("Done sleeping!")


# Try it
# slow_function()


# 6. DECORATORS WITH ARGUMENTS
# What if your function takes parameters?
# Use *args and **kwargs to handle any arguments

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(5, 3))  # Works with arguments!

# 7. PRESERVING FUNCTION METADATA
# Decorators hide the original function's name and docstring
# Use functools.wraps to fix this

from functools import wraps


def my_decorator(func):
    @wraps(func)  # This preserves the original function's metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(name):
    """Says hello to someone"""
    return f"Hello {name}!"


print(greet.__name__)  # Output: greet (not wrapper!)
print(greet.__doc__)  # Output: Says hello to someone


# 8. DECORATOR WITH ARGUMENTS
# What if you want to pass arguments to the decorator itself?
# You need another level of nesting (decorator factory)

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(times=3)
def say_hi():
    print("Hi!")


# Try it
# say_hi()  # Prints "Hi!" three times


# 9. PRACTICAL EXAMPLE: DEBUG DECORATOR
# Automatically log function calls with their arguments

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join(repr(a) for a in args)
        kwargs_str = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))

        print(f"Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result

    return wrapper


@debug
def multiply(x, y):
    return x * y


# Try it
# multiply(5, 3)


# 10. STACKING DECORATORS
# You can apply multiple decorators to one function
# They execute from bottom to top (closest to function first)

def bold(func):
    @wraps(func)
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper


def italic(func):
    @wraps(func)
    def wrapper():
        return f"<i>{func()}</i>"

    return wrapper


@bold
@italic
def greet():
    return "Hello!"


print(greet())  # Output: <b><i>Hello!</i></b>


# 11. CLASS-BASED DECORATORS
# You can also create decorators using classes

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello!")


# Try it
# say_hello()
# say_hello()
# say_hello()


# 12. COMMON USE CASES

# A. Authentication/Authorization
def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # In real app, check if user is logged in
        is_authenticated = True  # Simplified
        if not is_authenticated:
            raise PermissionError("User not authenticated")
        return func(*args, **kwargs)

    return wrapper


# B. Caching/Memoization
def cache(func):
    cached_results = {}

    @wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print(f"Returning cached result for {args}")
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result

    return wrapper


@cache
def expensive_calculation(n):
    print(f"Calculating {n}...")
    return n * n


# Try it
# print(expensive_calculation(5))
# print(expensive_calculation(5))  # Uses cached result


# C. Validation
def validate_positive(func):
    @wraps(func)
    def wrapper(x):
        if x <= 0:
            raise ValueError("Number must be positive")
        return func(x)

    return wrapper


@validate_positive
def square_root(x):
    return x ** 0.5


"""
===========================
QUICK REFERENCE CHEAT SHEET
===========================

-------------------------
Basic Decorator Template:
-------------------------
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper


----------------------------------
Decorator with Arguments Template:
----------------------------------
def decorator_with_args(arg1, arg2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use arg1, arg2 here
            return func(*args, **kwargs)
        return wrapper
    return decorator

-------------------------------
Class-Based Decorator Template:
-------------------------------
class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Do something
        return self.func(*args, **kwargs)

----------------
Common Patterns:
----------------
@timer              # Measure execution time
@cache              # Cache results
@debug              # Log function calls
@require_auth       # Check authentication
@validate           # Validate inputs
@retry              # Retry on failure
@rate_limit         # Limit call frequency

------------------
Notes to Remember:
------------------
- Decorators are just functions that modify other functions
- Always use @wraps to preserve metadata
- Use *args and **kwargs to handle any arguments
- Decorators execute at function definition time, not call time
- Stack decorators from bottom to top

----------------
Common Mistakes:
----------------
1. Forgetting to return the result in wrapper
2. Not using @wraps (loses function metadata)
3. Forgetting parentheses with decorator arguments
4. Not handling *args/**kwargs properly

-----------------------
When to Use Decorators:
-----------------------
✓ You're repeating the same setup/teardown code
✓ You need to modify behavior across many functions
✓ You want to enforce rules (auth, validation)
✓ You need to track or log function behavior
✗ The logic is complex and hard to understand
✗ You only need it in one place
✗ It makes debugging harder


"""
