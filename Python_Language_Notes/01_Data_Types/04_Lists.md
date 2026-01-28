# Lists in Python (`list`)

A **List** is a versatile, **mutable** collection of items. It is ordered, meaning items are stored in a specific sequence, and allows duplicate elements.

**Syntax**: `[item1, item2, ...]`

```python
l = [10, 20, 30, "Hello", 3.14]
```

---

## 1. Characteristics
*   **Ordered**: Items maintain their position.
*   **Mutable**: You can change, add, or remove items after creation.
*   **Heterogeneous**: Can hold mixed data types (int, str, float, etc.).
*   **Allow Duplicates**: `[1, 1, 2]` is valid.

---

## 2. Indexing and Slicing
Lists support indexing and slicing just like strings.

```python
a = [10, 20, 30, 40, 50]

# Indexing
print(a[0])    # 10
print(a[-1])   # 50

# Slicing
print(a[1:4])  # [20, 30, 40]
# Explanation: Starts at index 1 (20), up to but not including index 4 (50).

print(a[-4:-1]) # [20, 30, 40]
# Explanation: Starts at -4 (20), goes to -1 (50, exclusive).
```

---

## 3. Nested Lists
A list can contain another list.

```python
# List containing INT, Float tuple, and Set
s5 = [10, 20, (100, 200, 'Hello'), {1, 2, 3}]

# Accessing Nested Elements
# Fetch 100
print(s5[2][0])  # 100
# s5[2] is (100, 200, 'Hello')
# [0] refers to the first item of that tuple.

# Fetch 200
print(s5[2][1])  # 200
```

### Lab Scenario: Deeply Nested Indexing
*From your notes (`list.p.py`)*

```python
# Accessing 'Pandey Ji' and 'Yadav ji'
l6 = [1, 2.2, [2+2j, True, ['Yadav ji', 'Pandey Ji', False]]]

# Step 1: Access the innermost list
print(l6[2][2])
# Output: ['Yadav ji', 'Pandey Ji', False]

# Step 2: Access specific elements
print(l6[2][2][0])   # 'Yadav ji'
print(l6[2][2][1])   # 'Pandey Ji'

# Using Negative Indexing for the same:
print(l6[-1][-1][1]) # 'Pandey Ji'
```

---

## 4. List Copying
Copying lists can be tricky (Shallow vs Deep Copy).
👉 **[Read detailed notes on Copying here](04_List_Copying.md)**

---

## 5. Common Traps ⚠️

### Trap: Converting Float to List
You cannot directly convert a float to a list because floats are not iterable.

```python
list(6.46)   # ❌ TypeError: 'float' object is not iterable

# ✅ Correct way: Float -> String -> List
x = 6.46
result = list(str(x))
print(result) # ['6', '.', '4', '6']
```
