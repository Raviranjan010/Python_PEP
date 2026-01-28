# 📦 Tuples and Sets

## 1. Tuples (`tuple`)
A Tuple is an **ordered** and **immutable** collection of elements.

**Syntax**: `(item1, item2)`

```python
t = (10, 20, "Hello")
```

### 🔹 Characteristics
*   **Immutable**: Once created, you cannot change, add, or remove elements.
*   **Faster**: Tuples are faster than lists due to immutability.
*   **Single Element Trap**:
    ```python
    t1 = (10)   # ❌ This is an INT
    t2 = (10,)  # ✅ This is a TUPLE (comma is mandatory)
    ```

### 🔹 When to use?
Use tuples for data that should not change (e.g., coordinates, configuration constants).

---

## 2. Sets (`set`)
A Set is an **unordered** collection of **unique** items.

**Syntax**: `{item1, item2}`

```python
s = {1, 2, 3, 3, 2}
print(s) # {1, 2, 3} (Duplicates removed automatically)
```

### 🔹 Characteristics
*   **Unordered**: No index access (`s[0]` is ❌ Error).
*   **No Duplicates**: Automatically removes repeated values.
*   **Mutable**: You can add/remove items, but elements inside must be immutable.

### 🔹 Set Operations (VVI)
Sets support mathematical operations.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (All elements)
print(A | B) # {1, 2, 3, 4, 5, 6}

# Intersection (Common elements)
print(A & B) # {3, 4}

# Difference (A but not B)
print(A - B) # {1, 2}
```

---

## 🎯 VVI Interview Questions

### Q1. Can we modify a Tuple?
No, tuples are immutable. However, if a tuple contains a mutable item (like a list), that item can be modified.
```python
t = (1, [10, 20])
t[1][0] = 99  # ✅ Allowed!
print(t)      # (1, [99, 20])
```

### Q2. How to create an empty set?
```python
s = {}      # ❌ This is a DICTIONARY
s = set()   # ✅ This is an empty SET
```

### Q3. Why can't we access Set elements by index?
Sets are unordered. The data is stored using Hashing, not position.

### Q4. Can a Set contain a List?
**No**. Lists are mutable and unhashable. Sets can only contain immutable types (int, str, tuple).