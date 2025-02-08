# PYTHON CONDITIONAL STATEMENTS

"""
-------------------------------------------
Python Control Flow: Conditional Statements
-------------------------------------------
1. This section explains how to use conditional statements (if, elif, else) to control the flow of execution in Python.
"""

# 1. The 'if' statement:
# Executes a block of code only if a condition is true.

x = 10

if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# 2. The 'if-else' statement:
# Executes one block of code if a condition is true, and another block if it's false.

y = 3

if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")  # Output: y is not greater than 5


# 3. The 'if-elif-else' statement:
# Allows you to check multiple conditions.  'elif' stands for "else if".

z = 7

if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5")  # Output: z is greater than 5
elif z > 0:
    print("z is greater than 0")
else:
    print("z is not positive")


# 4. Nested Conditional Statements:
# You can put conditional statements inside other conditional statements.

age = 20
has_license = True

if age >= 18:
    print("You are old enough to drive.")
    if has_license:
        print("You have a driver's license.")  # Output: You have a driver's license.
    else:
        print("You need a driver's license.")  # Output: You need a driver's license. (If has_license was False)
else:
    print("You are not old enough to drive.")


# 5. Short Hand If:
# A concise way to write a simple if statement on a single line.

a = 15
if a > 10: print("a is greater than 10")  # Output: a is greater than 10

# 6. Short Hand If Else:
# A concise way to write a simple if-else statement on a single line (ternary operator).

b = 5
print("b is greater than 10") if b > 10 else print("b is not greater than 10") # Output: b is not greater than 10

# 7. Logical Operators in Conditions:
# You can use logical operators (and, or, not) to combine conditions.

p = 8
q = 12

if p > 5 and q > 10:
    print("Both p and q meet the conditions.")  # Output: Both p and q meet the conditions.

if p > 10 or q > 10:
    print("At least one of p or q meets the conditions.") # Output: At least one of p or q meets the conditions.

if not p > 10: # not inverts the condition
    print("p is not greater than 10") # Output: p is not greater than 10