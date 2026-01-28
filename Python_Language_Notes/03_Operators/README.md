# ⚙️ Operators in Python

Operators are symbols that perform operations on variables and values.

---

## 1. Arithmetic Operators
| Symbol | Name | Example | Result |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `10 + 2` | `12` |
| `-` | Subtraction | `10 - 2` | `8` |
| `*` | Multiplication | `10 * 2` | `20` |
| `/` | Division | `10 / 2` | `5.0` (Always Float) |
| `//` | Floor Division | `10 // 3` | `3` (Integer part) |
| `%` | Modulus | `10 % 3` | `1` (Remainder) |
| `**` | Exponentiation | `2 ** 3` | `8` (Power) |

---

## 2. Logical Operators (and, or, not)
Used for conditional logic.

### 🔹 `and`
Returns the **first False** value, or the **last** value if all are True.
```python
10 and 20   # 20 (Both true, returns last)
0 and 20    # 0  (First is false, returns 0)
```

### 🔹 `or`
Returns the **first True** value, or the **last** value if all are False.
```python
10 or 20    # 10 (First is true)
0 or 20     # 20 (First is false, check next)
```

### 🔹 `not`
Inverses the boolean value.
```python
not True    # False
not 0       # True
```

---

## 3. Identity Operators (`is`)
Compares **Memory Address**, not just value.

*   `is`: Returns True if both variables point to the same object.
*   `is not`: Returns True if they point to different objects.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (Values are equal)
print(a is b)  # False (Different memory locations)
print(a is c)  # True (Same memory location)
```

---

## 4. Membership Operators (`in`)
Checks if a value exists in a sequence (List, String, Tuple, Set, Dict Keys).

```python
l = [10, 20, 30]

print(10 in l)      # True
print(99 not in l)  # True
```

---

## 🎯 VVI Interview Questions

### Q1. Difference between `==` and `is`?
*   `==` compares **Values** (Content).
*   `is` compares **Memory Address** (Reference).

### Q2. What is the result of `True / 2`?
`0.5`. In Python, `True` is treated as `1` and `False` as `0` in arithmetic.

### Q3. Explain `//` vs `/`.
`/` always returns a float (e.g., `4/2 = 2.0`).
`//` returns the floor integer (e.g., `5//2 = 2`).

### Q4. Operator Precedence
`**` (Highest) -> `*, /, //, %` -> `+, -` -> `Relational` -> `Logical` (Lowest).