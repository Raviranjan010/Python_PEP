# 🧠 Type Casting in Python (Complete & Practical Guide)

Type casting means converting one data type into another. It is critical when working with user input, data processing, and real-world applications.

---

## 🔹 Why Type Casting Is Important (Real-World Scenario)

### 📌 User Input Case
By default, all input taken from the keyboard is a string.

```python
age = input("Enter age: ")
print(type(age))   # <class 'str'>
# Trying to perform calculations directly will fail.
```

### ✅ Correct Approach
Convert the string into an integer first:

```python
age = int(age)
print(age + 1)
```
➡️ **Without type casting, arithmetic operations will raise errors.**

---

## 🔹 String Type Casting

### ✅ String → Integer
✔ Possible only if the string represents a valid integer.

```python
int("10")     # ✅
int("+25")    # ✅
int("-8")     # ✅
```

### ❌ Invalid Conversions
```python
int("Python")   # ❌ ValueError: invalid literal for int()
int("10.5")     # ❌ ValueError: invalid literal (contains dot)
int("12a")      # ❌ ValueError
```

> **Rules**:
> 1. String must contain **only digits**.
> 2. `+` or `-` allowed only at the beginning.
> 3. **Decimal values are not allowed** (You must cast to float first: `int(float("10.5"))`).

### ✅ String → List / Tuple / Set
Each character is converted individually.

```python
s = "Python"

list(s)     # ['P', 'y', 't', 'h', 'o', 'n']
tuple(s)    # ('P', 'y', 't', 'h', 'o', 'n')
set(s)      # {'P', 'y', 't', 'h', 'o', 'n'} (Order random)
```

### ❌ String → Dictionary
```python
dict("Python")   # ❌ TypeError
```
> **Reason**: A dictionary requires **key–value pairs**, not single characters.

---

## 🔹 List Type Casting

### ❌ List → int / float / complex
```python
int([1, 2])      # ❌ TypeError
float([1, 2])    # ❌ TypeError
```
> **Reason**: Numeric types expect a **single value**, not a collection.

### ✅ List → String
```python
str([1, 2, 3])
# "[1, 2, 3]"  (The whole list becomes one string)
```

### ✅ List → Dictionary (VERY IMPORTANT)
Each element inside the list must:
1.  Be a collection (list / tuple / string).
2.  Have **exactly 2 elements** (key, value).

```python
dict(['ab', [20, 2], (40, 10)])
# {'a': 'b', 20: 2, 40: 10}
```

### ❌ Invalid Case (Length > 2)
```python
dict(['abc'])
# ValueError: dictionary update sequence element has length 3; 2 is required
```

### 📌 Key Override Rule
If duplicate keys exist, the **last value** overrides the previous one.
```python
dict(['ab', (20, 2), (20, 5)])
# {'a': 'b', 20: 5}
```

---

## 🔹 Tuple Type Casting

```python
t1 = (2.3, 22, 2, 55, "RaviRaj", False)
```

### ✅ Tuple → List / Set / String
```python
list(t1)
set(t1)
str(t1)
```

### ❌ Tuple → Dictionary
```python
dict(t1)   # ❌ TypeError
```
> **Reason**: Tuple elements are not key–value pairs.

---

## 🔹 Set Type Casting

```python
s1 = {1, 2, 3, 4}
```

### ❌ Set → int / float
```python
int(s1)     # ❌ TypeError
float(s1)   # ❌ TypeError
```

### ✅ Set → List / Tuple / String
```python
list(s1)
tuple(s1)
str(s1)
```

### ❌ Set → Dictionary
```python
dict(s1)    # ❌ TypeError
```
> **Reason**: Set contains single values, not key–value pairs.

---

## 🔹 Dictionary Type Casting

```python
d1 = {'a': 10, 'b': 20, 'c': 30}
```

### ✅ Dictionary → Boolean
```python
bool(d1)    # True (Any non-empty dictionary is True)
bool({})    # False
```

### ✅ Dictionary → List / Tuple / Set
By default, only **keys** are converted.
```python
list(d1)      # ['a', 'b', 'c']
tuple(d1)     # ('a', 'b', 'c')
set(d1)       # {'a', 'b', 'c'}
```

### 🔹 Dictionary Values & Items
```python
list(d1.values())   # [10, 20, 30]
list(d1.items())    # [('a', 10), ('b', 20), ('c', 30)]
```

---

## ⚠️ Common Interview Mistakes (VERY IMPORTANT)

| Mistake | Correction |
| :--- | :--- |
| **"Strings cannot be typecasted to int"** | Wrong. **Numeric** strings CAN be converted. |
| **Using `string()` function** | Wrong. The correct function is `str()`. |
| **Forgetting Dict requirements** | Dicts ALWAYS need key-value pair inputs (length 2). |
| **`bool()` validates logic** | Wrong. `bool()` only checks if a container is **empty** or **not**. |

---

## 🎯 VVI Interview Questions

### Q1. Can we convert "Python" into int?
❌ **No** — it is non-numeric.

### Q2. Why does `int(3.9)` return `3`?
✔ Decimal part is **truncated**, not rounded.

### Q3. Why does `dict(['abc'])` give an error?
✔ Length must be **exactly 2** for key–value pairs. `'abc'` has length 3.

### Q4. What does `bool({})` return?
✔ **False** — it is an empty dictionary.

### Q5. What happens if duplicate keys exist in conversion?
✔ The **last value** overrides the previous one. `dict([('a', 1), ('a', 2)])` -> `{'a': 2}`.

---
👉 **[Run Lab Examples](lab_type_casting.py)**
