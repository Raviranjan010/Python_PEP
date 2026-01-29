"""
List Copying Lab - Examples and Explanations
Covers: Assignment, Shallow Copy, and Deep Copy.
"""
import copy

# ==========================================
# 1. Assignment (Reference)
# ==========================================
l1 = [1, 2, 3]
l2 = l1  # Both point to same memory
l2[0] = 99
print(f"Assignment - l1: {l1}")  # [99, 2, 3] (Changed!)


# ==========================================
# 2. Shallow Copy (.copy())
# ==========================================
# Creates a new list, but inner elements are still references if they are mutable.
original = [1, 2, [100, 200]]
shallow = original.copy()

# Modifying outer element -> Independent
shallow[0] = 999

# Modifying inner element -> Affects BOTH
shallow[2][0] = 'Changed'

print(f"Shallow Original: {original}") # [1, 2, ['Changed', 200]]
print(f"Shallow Copy:     {shallow}")  # [999, 2, ['Changed', 200]]


# ==========================================
# 3. Deep Copy
# ==========================================
# Recursively copies everything. Complete independence.
deep = copy.deepcopy(original)
deep[2][0] = 'DeepChange'
print(f"Deep Original: {original}") # Unchanged by deep copy modification