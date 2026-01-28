# 📖 Dictionaries in Python (`dict`)

A **Dictionary** is an unordered collection of **Key-Value** pairs. It is mutable and does not allow duplicate keys.

**Syntax**: `{key: value, key2: value2}`

```python
d = {
    "name": "Python",
    "version": 3.14,
    "is_awesome": True
}
```

---

## 1. Key Characteristics
*   **Unordered**: (Historically). From Python 3.7+, insertion order is preserved, but you should access by Key, not index.
*   **Mutable**: Values can be changed.
*   **Keys**: Must be **Immutable** (int, float, str, tuple). You cannot use a list as a key.
*   **Values**: Can be anything (mutable or immutable).

---

## 2. Accessing Elements
Dictionaries do not use numeric indexing (0, 1, 2). They use **Keys**.

```python
d = {1: 'A', 'b': 'Ball'}

print(d[1])   # Output: 'A'
print(d['b']) # Output: 'Ball'

# ❌ Error
# print(d[0]) # KeyError (unless 0 is a key)
```

---

## 3. Nested Dictionaries & Complex Access
*From Lab Logs*

```python
d4 = {
    1: 10,
    'a': {2.2, 10, (20+2j)},  # Set inside Dict
    'b': ['Hi', 10]           # List inside Dict
}

# Fetch 'Hi'
print(d4['b'][0])  # 'Hi'

# Fetch Reverse of 'Hi'
print(d4['b'][0][::-1]) # 'iH'
```

---

## 4. Common Methods

| Method | Description |
| :--- | :--- |
| `d.keys()` | Returns list of keys. |
| `d.values()` | Returns list of values. |
| `d.items()` | Returns list of (key, value) tuples. |
| `d.get(key)` | Returns value. Returns `None` if key not found (Safe). |
| `d.pop(key)` | Removes key and returns value. |

---

## 🎯 VVI Interview Questions

### Q1. What happens if we define duplicate keys?
The **last** assignment wins. The previous value is overwritten.
```python
d = {'a': 1, 'a': 2}
print(d) # {'a': 2}
```

### Q2. Can we use a List as a Dictionary Key?
**No**. Lists are mutable and unhashable.
```python
d = {[1,2]: "Value"} # ❌ TypeError: unhashable type: 'list'
```

### Q3. How to merge two dictionaries?
Use the `|` operator (Python 3.9+) or `update()`.
```python
d1 = {'a': 1}
d2 = {'b': 2}
d3 = d1 | d2  # {'a': 1, 'b': 2}
```