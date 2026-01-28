# Tuples in Python (`tuple`)

A **Tuple** is similar to a list but is **immutable**. Once defined, you cannot change its elements (no adding, removing, or modifying).

**Syntax**: `(item1, item2, ...)`

```python
t = (10, 20, 30)
```

---

## 1. Single Element Tuple (The Trap)
A common confusion arises when creating a tuple with a single element. You **must** include a comma.

```python
# Integers
t1 = (10)   # <class 'int'> (Math grouping)
t2 = (10,)  # <class 'tuple'> (Tuple syntax)

# Strings
s1 = ('hello')  # <class 'str'>
s2 = ('hello',) # <class 'tuple'>
```
> **Rule**: "Parentheses do not make a tuple, comma makes a tuple."

---

## 2. Why use Tuples?
*   **Faster**: Tuples are slightly faster than lists due to immutability.
*   **Data Integrity**: Used for data that should not change (e.g., coordinates, configuration constants).
*   **Dictionary Keys**: Tuples can be used as keys in dictionaries (lists cannot).

---

## 3. Operations
*   **Indexing/Slicing**: Works exactly like lists.
*   **Immutability Check**:
    ```python
    t = (1, 2, 3)
    # t[0] = 100  --> TypeError: 'tuple' object does not support item assignment
    ```

---

## 4. Reversing a Tuple (Slicing)
```python
s3= ['Hello class', (5.2+2.36j, 11, False), {'a':101}]

# Fetch the reverse of the inner tuple
rev = s3[1][::-1]
print(rev)
# Output: (False, 11, (5.2+2.36j))
```
