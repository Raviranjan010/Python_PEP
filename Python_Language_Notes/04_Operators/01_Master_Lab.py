# 🧪 Python Master Lab - Data Types & Operators
# This file contains runnable examples based on your learning notes.

# ==========================================
# 1. LISTS & NESTED INDEXING
# ==========================================
print("--- Lists ---")
l6 = [1, 2.2, [2+2j, True, ['Yadav ji', 'Pandey Ji', False]]]

# Goal: Access 'Pandey Ji'
# Logic: l6[2] -> Inner List -> [2] -> Innermost List -> [1]
print(l6[2][2][1])  # Output: Pandey Ji

# Negative Indexing equivalent
print(l6[-1][-1][1])


# ==========================================
# 2. DICTIONARY TRAPS
# ==========================================
print("\n--- Dictionaries ---")

# Duplicate Keys Override
d = {1: 'First', 1: 'Second'}
print(d)  # {1: 'Second'} -> Last value wins

# Complex Nesting
d4 = {
    'a': {2.2, 10, (20+2j)}, # Set (Unordered)
    'b': ['Hi', 10]          # List (Ordered)
}

# Fetching from List inside Dict
print(d4['b'][0])       # 'Hi'
print(d4['b'][0][::-1]) # 'iH' (Reverse String)


# ==========================================
# 3. OPERATOR QUIRKS
# ==========================================
print("\n--- Operators ---")

# Logical AND/OR with Non-Booleans
print(10 and 20)  # 20 (Both true, return last)
print(0 and 20)   # 0  (First false, return first)
print(10 or 20)   # 10 (First true, return first)

# Comparison
print([10, 20] > [1, 2])   # True (10 > 1)
print([10, 20] > [10, 20]) # False (Equal)


# ==========================================
# 4. TYPE CASTING
# ==========================================
print("\n--- Type Casting ---")

# List to Dict (Requires pairs)
data = [['a', 1], ['b', 2]]
print(dict(data)) # {'a': 1, 'b': 2}

# String to List
s = "Python"
print(list(s)) # ['P', 'y', 't', 'h', 'o', 'n']