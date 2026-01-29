# 🔄 List Copying in Python: Reference vs Shallow vs Deep Copy

> **Exam & Interview Gold**: Understanding how Python copies lists is critical for avoiding bugs in nested data.

---

## 1. General Assignment (Reference Copy)
**"It points to the same memory"**

When you assign one list to another using `=`, you are **not** creating a new copy. You are just creating a new reference (alias) to the **same** memory location.

```python
L = [1, 2, 3]
a = L         # 'a' points to the same object as 'L'

a[0] = 99     # Modifying 'a' changes 'L' too!

print(L)      # [99, 2, 3]
print(a)      # [99, 2, 3]
```

*   **Memory**: Both variables point to the same Box.
*   **Result**: Changes in one affect the other.

---

## 2. Shallow Copy
**"Creates content value space and creates new memory layer"**

A shallow copy creates a **new** outer list. For simple (flat) lists, this makes them independent.

**Methods**:
1.  `list.copy()`
2.  Slicing `[:]`

### Example 1: Flat List (Independent)
```python
L = [1, 2, 3]
a = L.copy()  # Creates a new independent list

a[2] = 23

print(L) # [1, 2, 3]  (Original is SAFE)
print(a) # [1, 2, 23] (Only copy changed)
```

### Example 2: Nested List (Dependent!)
If the list contains other lists (nested), a shallow copy only copies the *reference* to the inner list. The inner list is **shared**.

```python
l2 = [1, 2, 3, [2, 3, 2], 7]
l4 = l2.copy()

# Modifying the inner list affects BOTH
l4[3][0] = 999 

print(l2) # [1, 2, 3, [999, 3, 2], 7] (Changed!)
print(l4) # [1, 2, 3, [999, 3, 2], 7]
# "Inside nested list does affect both values"
```

---

## 3. Deep Copy
**"Does not copy variable space and value space only, it creates a fully independent clone"**

A deep copy creates a completely independent clone of the original object and **recursively** copies all nested objects.

**Required**: `import copy`

```python
import copy

l = [1, 2, 33, 4, 7]
y = copy.deepcopy(l) # Creates fully independent copy

# Modify original
l[3] = 77

print(l) # [1, 2, 33, 77, 7]
print(y) # [1, 2, 33, 4, 7]
# "In this both become independent"
```

---

## 📊 Summary Table

| Type | Syntax | Outer Level | Nested Level |
| :--- | :--- | :--- | :--- |
| **Reference** | `a = b` | Same | Same |
| **Shallow** | `b.copy()` | New | Same (Shared) |
| **Deep** | `copy.deepcopy(b)` | New | New (Independent) |
