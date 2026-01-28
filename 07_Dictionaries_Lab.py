"""
Dictionary Lab - Examples and Explanations
Based on recent session.
"""

# ---------------------------------------------------------
# 1. Dictionary Creation & Key Overriding
# ---------------------------------------------------------
# If a key is used more than once, the last value overrides the previous ones.
# Note: True and 1 are considered the same key (True == 1).
d2 = {True: 33, 2: False}
print(f"d2: {d2}")  
# Output: {True: 33, 2: False}

d3 = {1: 33, "a": "Acsa", 5: 43}
print(f"d3: {d3}")
print(f"Type of d3: {type(d3)}")

# ---------------------------------------------------------
# 2. Accessing Elements
# ---------------------------------------------------------
print(f"Value of 'a': {d3['a']}")  # 'Acsa'
print(f"Value of 5: {d3[5]}")      # 43

# Accessing a non-existent key raises KeyError
try:
    print(d3[3])
except KeyError as e:
    print(f"Error accessing d3[3]: {e}")

# ---------------------------------------------------------
# 3. Nested Indexing
# ---------------------------------------------------------
# Accessing characters inside a string value
# d3['a'] is 'Acsa'
print(f"2nd index of d3['a']: {d3['a'][2]}")  # 's'
print(f"3rd index of d3['a']: {d3['a'][3]}")  # 'a'

# ---------------------------------------------------------
# 4. Complex Nested Dictionary
# ---------------------------------------------------------
# Note on Tuples: (10) is an int, (10,) is a tuple.
d4 = {
    1: 10, 
    2: 2.25, 
    2.2: 3+22j, 
    4: False, 
    'a': {2.2, 10, (20+2j)},  # Set (unordered)
    'b': ['Hi', 10]           # List (ordered)
}

# Fetching 'Hi' from list inside dictionary
a1 = d4['b']
print(f"First element of d4['b']: {a1[0]}")  # 'Hi'

# Fetching False
print(f"Value at key 4: {d4[4]}")  # False

# Fetching 2.2 from the set at d4['a']
# Sets are unordered and do not support indexing.
# We cannot use d4['a'][0]. We must iterate or check membership.
print(f"Set at d4['a']: {d4['a']}")

# ---------------------------------------------------------
# 5. Modifying Dictionaries
# ---------------------------------------------------------
d = {1: 'Das', 2: 4}
d[1] = "Alia"    # Update existing key
d[7] = 'Thala'   # Add new key
print(f"Modified d: {d}")

# Removing elements using pop()
removed_value = d.pop(1)
print(f"Popped value: {removed_value}")
print(f"d after pop: {d}")