"""
Type Casting Lab - Examples and Explanations
Covers: String to Int, List to Dict, and common conversion errors.
"""

# ==========================================
# 1. String to Integer
# ==========================================
# int('23.3') -> Error
# Reason: int() expects a string looking like an integer. 
# It cannot parse decimals directly from a string.
try:
    print(int('23.3'))
except ValueError as e:
    print(f"Error converting '23.3' to int: {e}")

# Correct way: String -> Float -> Int
print(f"Correct conversion: {int(float('23.3'))}")  # 23


# ==========================================
# 2. List to Dictionary
# ==========================================
# Rule: To convert a list to a dict, the list must contain inner sequences
# where each sequence has EXACTLY 2 elements (Key, Value).

data_valid = [['ab', [20, 2]], (40, 10)]
print(f"Valid Dict: {dict(data_valid)}")

# Error: Inner element has length 3
# dict(['abc', ...]) -> 'abc' has 3 characters.
try:
    dict(['abc', [20, 2]])
except ValueError as e:
    print(f"Error (Length 3): {e}")

# Error: Inner element has length 4
try:
    dict(['abcd', [20, 2]])
except ValueError as e:
    print(f"Error (Length 4): {e}")

# Key Override in Conversion
# If keys are repeated, the last one wins.
data_override = [['a', 1], ['a', 99]]
print(f"Override result: {dict(data_override)}")  # {'a': 99}


# ==========================================
# 3. Set Conversions
# ==========================================
s1 = {1, 2, 3, 4, 5}

# Set -> Int/Float (Error)
# Reason: Sets are collections, cannot be converted to a single number.

# Set -> Dict (Error)
# Reason: Sets do not have key-value pairs.

print(f"Set to List: {list(s1)}")