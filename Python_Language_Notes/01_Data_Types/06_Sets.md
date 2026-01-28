# Sets in Python (`set`)

A **Set** is an **unordered** collection of **unique** elements. It does **not** support indexing or slicing.

**Syntax**: `{item1, item2, ...}`

```python
s = {1, 2, 3, 4}
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
