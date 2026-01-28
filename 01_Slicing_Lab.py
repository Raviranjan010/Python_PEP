"""
Slicing Lab - Examples and Explanations
Based on recent session.
"""

# ---------------------------------------------------------
# 1. List Slicing
# ---------------------------------------------------------
a = [10, 20, 30, 40, 50]

# Positive Slicing: [start : end]
# Start is inclusive, End is exclusive.
print(f"a[1:4]: {a[1:4]}")  # [20, 30, 40]

# Negative Slicing
# Indices: -5(10), -4(20), -3(30), -2(40), -1(50)
print(f"a[-4:-1]: {a[-4:-1]}")  # [20, 30, 40]

# ---------------------------------------------------------
# 2. String Slicing
# ---------------------------------------------------------
s = 'Dictionary'

# Full string
print(f"s[::1]: {s[::1]}")

# Reverse string
print(f"s[::-1]: {s[::-1]}")  # 'yranoitciD'

# Substring
print(f"s[0:5]: {s[0:5]}")  # 'Dicti'

# ---------------------------------------------------------
# 3. Tricky Negative Slicing
# ---------------------------------------------------------
# s[-1:-4] returns empty string because default step is +1 (Left -> Right).
# -1 is the last element, -4 is to the left. You cannot go Left -> Right from -1 to -4.
print(f"s[-1:-4] (Empty): '{s[-1:-4]}'")

# To go backwards, we MUST specify a negative step.
print(f"s[-4:-1]: {s[-4:-1]}")  # 'nar'
print(f"s[-1:-5:-1]: {s[-1:-5:-1]}")  # 'yran'

# Advanced Step
s2 = 'Dictionary'
# Start -1, End -10, Step -2
print(f"s2[-1:-10:-2]: {s2[-1:-10:-2]}")  # 'yaoti'

# ---------------------------------------------------------
# 4. Nested Slicing
# ---------------------------------------------------------
s3 = ['Hello class', (5.2+2.36j, 11, False), {'a': 101, 10.1: 5500}]

# Fetch reverse of the tuple at index 1
# s3[1] is the tuple. [::-1] reverses it.
rev = s3[1][::-1]
print(f"Reverse tuple: {rev}")

# Nested List/Tuple/Set
s5 = [10, 20, (100, 200, 'Hello'), {1, 2, 3}]
print(f"s5[2][0]: {s5[2][0]}")  # 100
print(f"s5[2][1]: {s5[2][1]}")  # 200

# String inside List inside Dictionary
s7 = {'a': ["This is a list"], 'b': [10, 20, 30, ("Hello", 'Guys')]}
# Fetch reverse of 'Guys'
# s7['b'][3][1] is 'Guys'
# 'Guys' reversed is 'syuG'
print(f"Reverse 'Guys': {s7['b'][3][1][::-1]}")