# Accessing String Characters in Python

"""
-----------------------------------
Python: Accessing String Characters
-----------------------------------

1. Python allows you to access individual characters in a string using INDEXING and extract portions of a string using SLICING.
Strings are zero-indexed, meaning the first character is at position 0.

--------------
** Indexing **
--------------
1. Indexing helps you retrieve specific characters from a string. You can use both positive and negative indices.
2. Positive indices (0, 1, 2, ...) start from the beginning of the string.
3. Negative indices (-1, -2, -3, ...) start from the end of the string.
4. Indexing Syntax for Strings: string_variable[index-value]

-------------
** Slicing **
-------------
1. Slicing allows you to extract parts of a string using the syntax.
2. Slicing Syntax for Strings: string[start:end:step].
*  start: The starting index.
*  end: The stopping index.
*  step: The step value (optional, default is 1).
3. Slicing Syntax for Strings: string_variable[start:stop:step]
"""

# ACCESSING CHARACTERS iN A STRING USING INDEXING

first_name = "Sally"  # Define a string variable

# Access character at index 1 (second character)
print(first_name[1])  # Output: a

# Access character at index -2 (second last character)
print(first_name[-2])  # Output: l

# SLICING A STRING TO EXTRACT SUBSTRINGS

greeting = "I love learning Python"

# Basic Slicing (Extracting substrings)
first_word = greeting[0:1]  # 'I' (First character)
first_five_chars = greeting[0:5]  # 'I lov' (Indexes 0 to 4)
without_first_word = greeting[2:]  # 'love learning Python' (Excludes first character and space)
without_last_word = greeting[:-7]  # 'I love learning' (Excludes ' Python')

# Slicing with Step
every_second_char = greeting[::2]  # 'Ilv erigPto' (Every second character)
skip_three_chars = greeting[::3]  # 'IoennPh' (Every third character)

# Negative Step (Reversing)
reversed_greeting = greeting[::-1]  # 'nohtyP gninrael evol I'
reverse_every_second_char = greeting[::-2]  # 'nhy nnrelvI'

# Custom Ranges
middle_part = greeting[7:15]  # 'learning' (Indexes 7 to 14)
end_part = greeting[-6:]  # 'Python' (Last 6 characters)


