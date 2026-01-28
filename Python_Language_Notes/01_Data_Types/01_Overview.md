# Python Data Types: An Overview

## What are Data Types?
In programming, a **Data Type** specifies the type of value a variable can hold. It determines what operations can be performed on the data and how it is stored in memory.

Since Python is a **dynamically typed language**, you do not need to explicitly declare the type of a variable. The interpreter infers the type at runtime based on the value assigned.

```python
x = 10      # int
y = "Hello" # str
z = 3.14    # float
```

---

## Classification of Data Types

Python data types are broadly categorized into:

### 1. Fundamental (Primitive) Data Types
These are the basic building blocks.
*   **Numeric**:
    *   `int`: Integers (whole numbers), e.g., `10`, `-5`.
    *   `float`: Floating-point numbers (decimals), e.g., `3.14`, `-0.01`.
    *   `complex`: Complex numbers, e.g., `3 + 4j`.
*   **Boolean**:
    *   `bool`: Represents Truth values, `True` or `False`.
*   **None Type**:
    *   `None`: Represents the absence of a value (null).

### 2. Collection (Sequential) Data Types
These are used to store multiple values in a single variable.

| Type | Name | Mutable? | Ordered? | Duplicates? | Syntax |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **String** | `str` | ❌ No | ✅ Yes | ✅ Yes | `"Text"` |
| **List** | `list` | ✅ Yes | ✅ Yes | ✅ Yes | `[1, 2]` |
| **Tuple** | `tuple` | ❌ No | ✅ Yes | ✅ Yes | `(1, 2)` |
| **Set** | `set` | ✅ Yes | ❌ No | ❌ No | `{1, 2}` |
| **Dictionary** | `dict` | ✅ Yes | ✅ Yes* | ❌ No (Keys) | `{'k': 'v'}` |

*(Dictionaries are ordered since Python 3.7+)*

---

## Checking Data Types
You can use the `type()` function to check the data type of any variable.

```python
a = 100
print(type(a))  # Output: <class 'int'>

b = [1, 2, 3]
print(type(b))  # Output: <class 'list'>
```
