# 🧠 Type Casting in Python (Complete Guide)

Type casting (or Type Conversion) is the process of converting a literal or a variable from one data type to another. This is essential when handling user input, processing data from APIs, or performing mathematical operations on mixed types.

---

## 1. Fundamental Type Casting

### 🔹 Integer Casting (`int()`)
Converts a value into an integer.

*   **From Float**: Truncates the decimal part (does not round).
    ```python
    int(3.99)  # 3
    int(-2.5)  # -2
    ```
*   **From Boolean**:
    ```python
    int(True)  # 1
    int(False) # 0
    ```
*   **From String**:
    *   String must contain **only digits**.
    *   Optional `+` or `-` sign at the start is allowed.
    *   **No decimal points** allowed in the string.
    *   **No spaces** allowed inside the number.
    ```python
    int("10")    # 10
    int("-5")    # -5
    int("3.5")   # ❌ ValueError (String contains '.')
    int("10a")   # ❌ ValueError (Contains character)
    ```
    > **Trick**: To convert a string float like `"3.5"` to int, convert to float first: `int(float("3.5"))`.

### 🔹 Float Casting (`float()`)
Converts a value into a floating-point number.

*   **From Int**: Adds `.0`.
    ```python
    float(10)    # 10.0
    ```
*   **From String**: Can handle integers or decimal strings.
    ```python
    float("3.5") # 3.5
    float("10")  # 10.0
    ```

### 🔹 Boolean Casting (`bool()`)
Converts a value to `True` or `False`. This is based on **Truthiness**.

*   **Falsy Values (Result -> `False`)**:
    1.  Zero: `0`, `0.0`, `0j`
    2.  `None`
    3.  Empty Collections: `""` (Empty String), `[]`, `()`, `{}`, `set()`
*   **Truthy Values (Result -> `True`)**:
    *   Everything else (e.g., `1`, `-1`, `" "`, `[0]`, `{'a': 1}`).

```python
bool(0)      # False
bool("Hi")   # True
bool("False")# True (Non-empty string!)
bool({})     # False
```

### 🔹 Complex Casting (`complex()`)
*   `complex(real)` -> `real + 0j`
*   `complex(real, imag)` -> `real + imag*j`
*   `complex("3+4j")` -> `3+4j` (⚠️ No spaces allowed around `+` or `-` in string).

---

## 2. Collection Type Casting

### 🔹 String to List / Tuple / Set
Iterates over the string and treats each character as an element.

```python
s = "Python"

list(s)   # ['P', 'y', 't', 'h', 'o', 'n']
tuple(s)  # ('P', 'y', 't', 'h', 'o', 'n')
set(s)    # {'P', 'y', 't', 'h', 'o', 'n'} (Order is random)
```

### 🔹 List / Tuple / Set Inter-conversion
*   `list()`: Preserves order, allows duplicates.
*   `tuple()`: Preserves order, immutable.
*   `set()`: **Removes duplicates**, destroys order.

```python
nums = [1, 2, 2, 3]
print(set(nums))  # {1, 2, 3} (Unique elements)
```

---

## 3. Dictionary Casting (`dict()`) - ⚠️ The Tricky Part

To convert something into a dictionary, the data must be a **sequence of Key-Value pairs**.

### ✅ Valid Structures
The input must be a collection (list/tuple) where **every item** is a collection of **exactly 2 elements** (Key, Value).

```python
# List of Lists
l = [[1, 'a'], [2, 'b']]
dict(l)  # {1: 'a', 2: 'b'}

# List of Tuples
l = [(1, 'a'), (2, 'b')]
dict(l)  # {1: 'a', 2: 'b'}

# Tuple of Strings (Length 2 strings)
# 'ab' splits into 'a' (Key) and 'b' (Value)
l = ('ab', 'xy')
dict(l)  # {'a': 'b', 'x': 'y'}
```

### ❌ Invalid Structures
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


Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Type casting
>>> #s = "Python"  str->int => int(s) Error
>>> #It is not possible  to typecast string into integer
>>> int(3.3)
3
>>> #To convert a string into integer we must have only an integer value inside the string , if '+' or '-' sign is their , it must be at the beginning
>>> 
>>> #str-> list -> list(s)=['P','Y','T','H','O','N']
>>> #If we have multiple integer seperated with each other using comma or anything like ''then is works .
>>> #If we have multiple integer seperated with each other using comma or anything like ''then is works .
>>> # Q.convert string 'Ravi'into  list, set, dictionary , tuple, list into dictionary and convert all
>>> 
>>> list->int (error)
SyntaxError: invalid syntax
>>> #list->float (error)
>>> #list-> complex (error)
>>> #list->string ......
>>> 
>>> #list-> dict (error)
>>> 
>>> #To Typecast list into dictionary if  list values of list must be of collection data type and length of each value must be 2 eg:
>>> dict(['ab', [20,2],(40,10)])
{'a': 'b', 20: 2, 40: 10}
>>> dict(['abc', [20,2],(40,10)])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(['abc', [20,2],(40,10)])
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> dict(['ab', [20,2],(40,10), [20,5]])
{'a': 'b', 20: 5, 40: 10}
>>> #if we take more then 2 pair in any 2 same collection then it will give error
>>> #if we use same key then it will override
>>> dict(['ab', [20,2],(40,10), (20,5)])
{'a': 'b', 20: 5, 40: 10}
>>> dict(['abcd', [20,2],(40,10), [20,5]])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(['abcd', [20,2],(40,10), [20,5]])
ValueError: dictionary update sequence element #0 has length 4; 2 is required
dict(['2b', [20,2],(40,10), [20,5]])
{'2': 'b', 20: 5, 40: 10}
#Take example of tuple and typecase into other data type
t1=(2.3,22,2,55,"Ravi" 'Raj', False)
list(t1)
[2.3, 22, 2, 55, 'RaviRaj', False]
dict(l1)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dict(l1)
NameError: name 'l1' is not defined. Did you mean: 't1'?
set(t1)
{False, 2.3, 2, 22, 55, 'RaviRaj'}
dict(t1)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    dict(t1)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
#SET

s1={1,2,3,4,5,8,9}
int(s1)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(s1)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s1)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    float(s1)
TypeError: float() argument must be a string or a real number, not 'set'
string(s1)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    string(s1)
NameError: name 'string' is not defined. Did you forget to import 'string'?
list(s1)
[1, 2, 3, 4, 5, 8, 9]
tuple(s1)
(1, 2, 3, 4, 5, 8, 9)
dict(s1)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dict(s1)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
str(s1)
'{1, 2, 3, 4, 5, 8, 9}'

#DICTIONARY
#Dict -> bool
d1={'a':10,'b':20, 'c':30}
bool(d)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    bool(d)
NameError: name 'd' is not defined. Did you mean: 'd1'?
bool(d1)
True
#Give True because bool work as function that check weather values are default or not
str(d1)
"{'a': 10, 'b': 20, 'c': 30}"
list(d1)
['a', 'b', 'c']
tup(d1)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    tup(d1)
NameError: name 'tup' is not defined
tuple(d1)
('a', 'b', 'c')
set(d1)
{'c', 'b', 'a'}
list(d.values())
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    list(d.values())
NameError: name 'd' is not defined. Did you mean: 'd1'?
list(d1.values())
[10, 20, 30]
list(d1.items())
[('a', 10), ('b', 20), ('c', 30)]
tuple(d1.items())
(('a', 10), ('b', 20), ('c', 30))
