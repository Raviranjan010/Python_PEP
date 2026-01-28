"""
Sets Lab - Examples and Explanations
Based on recent session.
"""

# ---------------------------------------------------------
# 1. Union Operation
# ---------------------------------------------------------
a = {2, 3, 'Tina', 10+10j}
t = (10, 5)

# Note: set.union(t) raises TypeError because 'set' is the class.
# We must use an instance of a set to call union, or pass the set as the first argument.
# Correct: a.union(t)
result = a.union(t)
print(f"Union result: {result}")
# Result contains unique elements from both 'a' and 't'.

# ---------------------------------------------------------
# 2. Adding Elements
# ---------------------------------------------------------
# set.add() takes exactly one argument.
# The element must be immutable (hashable).

# Adding an integer
a.add(40)

# Adding a tuple (Immutable -> Allowed)
a.add((2, 22))

# Adding another tuple
a.add(("Raju", 3))

print(f"Updated Set: {a}")

# Note: We cannot add a list to a set because lists are mutable (unhashable).
# a.add([1, 2])  # Raises TypeError