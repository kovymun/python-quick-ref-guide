greeting = "hello learner"
print(greeting.upper())    # Output: "HELLO WORLD"
print(greeting.lower())    # Output: "hello world"

# ------------------------------------------------------------------------------------------------------------------------------------- #
"""
-------------
Split method: 
-------------
1. The split() method in Python is used to split a string into a LIST of substrings based on a specified delimiter (or seperator).
2. Examples of delimiters/seperators: comma(",") |  space (" ") | hyphen ("-") | pipe ("|")
3. By default, it splits on whitespace (spaces, tabs, or newlines).
4. SYNTAX: string.split(separator, maxsplit)
   * maxsplit: Specifies how many splits (or separations) to do. Default value = -1
"""

# Example using the split() method
greeting_sep = greeting.split() # default split (whitespaces)
print(greeting_sep) # Output: ['hello', 'learner']

# ------------------------------------------------------------------------------------------------------------------------------------- #
"""
--------------
Replace method:
--------------
1. The replace() method in Python is used to create a new string by replacing all occurrences of a specified substring with another substring.  The original string is *not* modified.
2. It's important to remember that strings in Python are immutable.  `replace()` creates and returns a *new* string with the replacements made.
3. SYNTAX: string.replace(old_substring, new_substring, count)
   * old_substring: The substring you want to replace.
   * new_substring: The substring you want to replace the old substring with.
   * count (optional):  Specifies how many occurrences to replace. If not specified, all occurrences are replaced.
"""

# Example using the replace() method

new_greeting = greeting.replace("learner", "beyonce")
print(new_greeting)  # Output: hello beyonce
print(greeting) # Output: hello learner (original string is unchanged)

# Replacing only the first occurrence:
greeting_again = "hello learner and hello world learner"
new_greeting_again = greeting_again.replace("learner", "artist", 1) #replace only the first occurrence of "learner" with "artist"
print(new_greeting_again) # Output: hello artist and hello world learner

# Replacing all occurrences:
new_greeting_all = greeting_again.replace("learner", "artist") #replace all occurrences of "learner" with "artist"
print(new_greeting_all) # Output: hello artist and hello world artist

"""

-------------
Strip method:
-------------
1. The strip() method in Python is used to remove leading and trailing whitespace (spaces, tabs, or newlines) from a string.
2. In simple terms, it removes the whitespaces from the beginning and end of string.
3. You can also specify a set of characters to remove from the beginning and end of the string.
4. If no argument is provided, it removes only whitespace.
5. SYNTAX: string.strip([characters])
   * characters (optional): Specifies a string of characters to be removed from both ends. If omitted, it defaults to whitespace.
"""

# Example using the strip() method
text = "   hello, learner!   "
clean_text = text.strip()  # Removes leading and trailing spaces
print(clean_text)  # Output: "hello, learner!"

# Example with a custom set of characters
custom_text = ",,,hello, learner!!!"
clean_custom_text = custom_text.strip(",!")  # Removes leading/trailing ',' and '!'
print(clean_custom_text)  # Output: "hello, learner"

