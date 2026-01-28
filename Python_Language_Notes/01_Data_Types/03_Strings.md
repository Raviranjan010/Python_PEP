# String Data Type (`str`)

A **String** is a sequence of characters enclosed in standard quotes. In Python, strings are **immutable**, meaning once created, they cannot be changed.

```python
s1 = 'Hello'
s2 = "World"
s3 = '''Multi-line
String'''
```

---

## 2. String Indexing
Accessing individual characters using their position (index).
*   **Positive Indexing**: Starts from `0` (Left to Right).
*   **Negative Indexing**: Starts from `-1` (Right to Left).

```python
s = "PYTHON"

#  P   Y   T   H   O   N
#  0   1   2   3   4   5  (Positive)
# -6  -5  -4  -3  -2  -1  (Negative)

print(s[0])   # 'P'
print(s[-1])  # 'N' (Last character)
```

### Lab Examples
*From your notes (`list.p.py`)*
```python
s = 'python'
print(s[-5])   # 'y'  (p -6, y -5, t -4, h -3, o -2, n -1)

s1 = 'This is python class'
print(s1[-11]) # 'y'  (Counting backwards from 's')
```

---

## 3. String Slicing
Slicing allows you to extract a substring by specifying a range.

**Syntax**: `string[start : end : step]`
*   **start**: Starting index (inclusive). Default is 0.
*   **end**: Ending index (exclusive). Default is length of string.
*   **step**: Jump count. Default is 1.

### Basic Slicing Rules
1.  **Positive Step** `(step > 0)`: Moves Left → Right. `end` index must be greater than `start`.
2.  **Negative Step** `(step < 0)`: Moves Right ← Left (Reverse). `start` index must be greater than `end`.
3.  **End is Exclusive**: Pythons stops *before* the end index.

### Examples (Derived from your notes)

#### Positive Slicing
```python
s = "Dictionary"
# D i c t i o n a r y
# 0 1 2 3 4 5 6 7 8 9

print(s[0:5])   # 'Dicti' (indices 0,1,2,3,4)
print(s[::1])   # 'Dictionary' (Full string)
```

#### Negative Slicing (Reverse)
> [!IMPORTANT]
> To slice backwards, you **must** specify a negative step (e.g., `-1`).
> Without a negative step, logical start must be left of end.

```python
s = "Dictionary"

# Reverse the string
print(s[::-1])  # 'yranoitciD'

# Slicing with negative indices
print(s[-1:-4:-1])
# Logic: Start at -1 ('y'), go towards -4 ('n'), step -1.
# Result: 'yra' (Indices -1, -2, -3)

# Common Mistake:
print(s[-1:-4]) # Output: '' (Empty)
# Reason: Default step is +1 (Left->Right), but -1 is to the right of -4.
# You cannot go from right to left with a positive step.
```

#### Advanced Examples
```python
s2 = 'Dictionary'
# step -2: Skip every alternate character in reverse
print(s2[-1:-10:-2])
# Sequence: -1(y), -3(a), -5(o), -7(t), -9(i)
# Output: 'yaoti'
```

---

## 4. Useful String Methods
Although strings are immutable, methods return a *new* string.

*   `upper()`: Converts to uppercase.
*   `lower()`: Converts to lowercase.
*   `strip()`: Removes whitespace from ends.
*   `replace(old, new)`: Replaces substring.
*   `split(delimiter)`: Splits string into a list.

```python
text = "  Hello Python  "
print(text.strip())       # "Hello Python"
print(text.lower())       # "  hello python  "
print(text.split())       # ['Hello', 'Python']
```
