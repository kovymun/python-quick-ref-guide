# PYTHON VARIABLES

# Defining a variable in Python
name = "James"  # This creates a variable called "name" and assigns it the value "James"
print(name)  # This prints the value of 'name' to the console

"""
-----------------
PYTHON VARIABLES:
-----------------

* A variable in Python is a named reference that stores data in memory.
* SYNTAX: identifier_name = value (snake case - most used convention in Python)
* EXAMPLE: first_name = "James"

----------------------------
VARIABLE NAMING CONVENTIONS:
----------------------------

1. Start with a letter or underscore (_): 
   - Correct: user_name, _age
   - Incorrect: 1user, -age

2. Use only alphanumeric characters and underscores (A-Z, a-z, 0-9, _):
   - Correct: user_age, account_balance
   - Incorrect: user-age, account#balance

3. Case-Sensitive:
   - username and UserName are treated as different variables.

4. Cannot be a reserved keyword:
   - Avoid using keywords like def, class, if, while, etc.

5. Readable and Descriptive:
   - Use meaningful names like total_score, customer_name instead of x or y.

---------------------------
NAMING CONVENTION STANDARD:
---------------------------

1. Snake Case (preferred in Python):
  - Words are separated by underscores.
  - Example: first_name, last_name

"""

"""
EXAMPLE:

An example of how we can use stored data (a.k.a. variables) is to calculate
the total price of an item, including tax, as shown below.
"""

cost = 100  # Base cost of the item
tax_percentage = 0.15  # 15% tax expressed as a decimal
tax_amount = cost * tax_percentage  # Calculate the tax amount
item_price = cost + tax_amount  # Final price including tax

print(f"Item price = {item_price}")
