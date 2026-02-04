# 📦 Sets in Python (`set`)

A **Set** is an **unordered** collection of **unique** and **immutable** elements. It is highly optimized for mathematical operations and membership testing.

**Syntax**: `{item1, item2, ...}`

```python
s = {10, 20, 30, 40}
```

---

## 1. Key Features
*   **Unordered**: Items have no fixed position; you cannot access them via `s[0]`.
*   **Unique**: Duplicates are automatically removed.
    ```python
    s = {1, 2, 2, 3}
    print(s)  # {1, 2, 3}
    ```
*   **Mutable**: You can add/remove items, but elements themselves must be immutable (you can't add a list to a set).

---

## 2. Creating an Empty Set
```python
s = {}      # This creates an empty DICTIONARY, not a set!
s = set()   # This creates an empty SET.
```

---

## 3. Basic Operations

### Adding Elements (`add` vs `update`)

1.  **`add()`**: Adds a **single** element.
    ```python
    s = {10, 20}
    s.add(30) # {10, 20, 30}
    ```
2.  **`update()`**: Adds **multiple** elements (from list, tuple, set, string).
    ```python
    s = {10, 20}
    s.update([30, 40]) # {10, 20, 30, 40}
    ```

> [!WARNING]
> `s.add([1, 2])` -> **TypeError** (Lists are unhashable/mutable).
> `s.update(10)` -> **TypeError** (Int is not iterable).

---

## 4. Set Difference (`-`)
The `-` operator in sets means **Difference**, not Arithmetic Subtraction.

*   `A - B`: Remove elements of B that are present in A.
*   If no common elements, A remains unchanged.

```python
{22, 33, 4} - {22}      # {33, 4} (22 removed)
{100, 20} - {"Hello"}   # {100, 20} (No match, no change)
{3, 4} - {3, 4}         # set() (All removed)
```
> **Rule**: "Set difference removes only common elements. Types don't matter, only equality."

---

### Union (Combining Sets)
```python
a = {1, 2, 3}
b = {3, 4, 5}

# Using method
print(a.union(b))  # {1, 2, 3, 4, 5}

# Using Operator
print(a | b)       # {1, 2, 3, 4, 5}
```

---

## 5. Lab Examples: String Decomposition
When converting specific strings to sets, remember that it splits characters and removes duplicates.

```python
# Case 1: "45.6"
print(set("45.6"))
# Output: {'4', '5', '.', '6'} (Order random)

# Case 2: "5.55"
print(set("5.55"))
# Output: {'5', '.'} (Duplicates '5' removed)
```
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