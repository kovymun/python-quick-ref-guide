# PYTHON STRING METHODS

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

"""
-------------------
Comprehensive List of Common Python String Methods:
-------------------
1. capitalize(): Converts the first character to uppercase.
2. casefold(): Converts string to lowercase more aggressively (useful for caseless comparisons).
3. center(width, fillchar): Centers the string in a field of given width.
4. count(substring, start, end): Returns the number of occurrences of a substring.
5. endswith(suffix, start, end): Returns True if the string ends with the specified suffix.
6. find(substring, start, end): Returns the index of the first occurrence. Returns -1 if not found.
7. index(substring, start, end): Same as find(), but raises ValueError if not found.
8. isalnum(): Returns True if all characters are alphanumeric.
9. isalpha(): Returns True if all characters are alphabetic.
10. isascii(): Returns True if all characters are ASCII.
11. isdecimal(): Returns True if all characters are decimal characters.
12. isdigit(): Returns True if all characters are digits.
13. isidentifier(): Checks if the string is a valid Python identifier.
14. islower(): Returns True if all cased characters are lowercase.
15. isnumeric(): Returns True if all characters are numeric.
16. isprintable(): Returns True if all characters are printable.
17. isspace(): Returns True if all characters are whitespace.
18. istitle(): Returns True if the string is in title case.
19. isupper(): Returns True if all cased characters are uppercase.
20. join(iterable): Joins the elements of an iterable with the string as separator.
21. ljust(width, fillchar): Left aligns the string.
22. lower(): Converts all characters to lowercase.
23. lstrip([chars]): Removes leading characters (default is whitespace).
24. partition(sep): Splits string into 3 parts: before sep, sep, after sep.
25. removeprefix(prefix): Removes the specified prefix if present.
26. removesuffix(suffix): Removes the specified suffix if present.
27. replace(old, new, count): Replaces old with new.
28. rfind(substring): Finds highest index of substring.
29. rindex(substring): Same as rfind but raises ValueError if not found.
30. rjust(width, fillchar): Right aligns the string.
31. rsplit(sep, maxsplit): Splits from the right.
32. rstrip([chars]): Removes trailing characters (default is whitespace).
33. split(sep, maxsplit): Splits the string.
34. splitlines(keepends): Splits at line breaks.
35. startswith(prefix, start, end): Checks if the string starts with the given prefix.
36. strip([chars]): Removes leading/trailing characters.
37. swapcase(): Swaps uppercase to lowercase and vice versa.
38. title(): Converts first letter of each word to uppercase.
39. translate(map): Translates characters using a translation table.
40. upper(): Converts string to uppercase.
41. zfill(width): Pads string on the left with zeros to reach the width.
"""