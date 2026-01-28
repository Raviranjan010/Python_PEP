# 🐍 Python Programming Language – Master Notes

> **Welcome!** This repository contains comprehensive notes, lab exercises, and interview questions for Python.

---

## 📚 Table of Contents

### 1. 🔰 Introduction
*   [Language Fundamentals](1_Language_Fundamentals.md) - High vs Low level, Compiler vs Interpreter.
*   [Features of Python](#-features-of-python-programming-language) - Why Python?

### 2. 🧬 Data Types
*   [Overview](../Python_Language_Notes/01_Data_Types/01_Overview.md) - Mutable vs Immutable, Classification.
*   [Lists](../Python_Language_Notes/01_Data_Types/04_Lists.md) - Creation, Indexing, Slicing, Nested Lists.
*   [List Copying](../Python_Language_Notes/01_Data_Types/04_List_Copying.md) - Shallow vs Deep Copy.
*   [Dictionaries](../Python_Language_Notes/01_Data_Types/07_Dictionaries.md) - Key-Value pairs, Methods.
*   [Tuples & Sets](../Python_Language_Notes/01_Data_Types/05_Tuples_Sets.md) - Immutable sequences and unique collections.

### 3. 🧠 Type Casting
*   [Type Casting Guide](../Python_Language_Notes/02_Type_Casting/README.md) - Converting between types (str -> int, list -> dict).

### 4. ⚙️ Operators
*   [Operators Overview](../Python_Language_Notes/03_Operators/README.md) - Arithmetic, Logical, Bitwise.
*   [Relational Operators](../Python_Language_Notes/03_Operators/02_Relational.md) - Comparison logic.

---

## 📌 Features of Python Programming Language

Python is a high-level, interpreted programming language known for its simplicity and versatility.

### 🔹 Key Features

- **Easy to Learn and Understand**  
  Python uses simple and readable syntax, making it beginner-friendly.

  ```python
  print("Hello World")
Dynamically Typed Language
No need to declare data types explicitly.
The data type of a variable is determined at runtime.

Interpreted Language
Python executes code line by line, which makes debugging easier.

🔁 Difference Between Compiler and Interpreter
Compiler	Interpreter
Translates entire code at once	Translates code line by line
Errors shown after full compilation	Stops execution at first error
Faster execution	Slower execution
Example: C, C++	Example: Python

Huge Number of Libraries
Python has a massive collection of libraries (7 Crore+ packages available via PyPI).

Platform Independent
Python programs can run on Windows, Linux, and macOS without modification.

High-Level Programming Language
Focuses more on problem-solving than hardware management.

Multi-Paradigm Support
Python supports multiple programming paradigms:

Procedural Programming

Object-Oriented Programming

Functional Programming

Open Source
Python is free to use and modify.

🌍 Domains Using Python
Python is widely used in the following domains:

Game Development

Cyber Security

Web Development

Automation

Cloud & DevOps

Robotics

Science & Research

Data Analysis

Generative AI

👨‍💻 Father of Python
Guido Van Rossum is known as the Father of Python.

📚 Python Library Components
Python libraries mainly include:

Keywords

Operators

Inbuilt Functions

🔑 Keywords in Python
Keywords are reserved words defined by Python developers.

They have predefined meanings and cannot be used as identifiers.

Example:
python
Copy code
import keyword
print(keyword.kwlist)
Important Notes:
True, False, and None are special keywords

They cannot be used as variable names

⚙️ Operators in Python
Python supports the following types of operators:

Arithmetic Operators

Logical Operators

Relational (Comparison) Operators

Assignment Operators

Membership Operators

Bitwise Operators

🧠 Inbuilt Functions
Some commonly used inbuilt functions:

len() → Returns the length of an object

id() → Returns the memory address of a variable

type() → Returns the data type of a variable

📌 Note:
Variables store values at hexadecimal memory addresses internally.

🆔 Rules of Identifiers
Identifiers are names given to variables, functions, etc.

Rules:
Must not be a keyword

No spaces allowed

Must not start with a number

Can contain only alphabets, digits, and _

Special characters are not allowed (except _)

Length should be less than 72 characters

🧬 Data Types in Python
🔹 Single-Valued (Individual) Data Types
Integer

Float

Complex

Boolean

Complex Number Example:

python
Copy code
a = 4 + 5j
Default Boolean Value:
False

🔹 Multi-Valued (Collection) Data Types
String

List

Tuple

Set

Dictionary

Frozenset

🔤 String Data Type
Strings can be created using:

' ' → General use

" " → When string contains single quotes

''' ''' → Multi-line strings

📌 Indexing in Python
Indexing is used to access elements from data types.

Types of Indexing
Positive Indexing → Left to Right

Negative Indexing → Right to Left

Syntax:
python
Copy code
variable_name[index]
Negative Index Formula:
text
Copy code
actual_index = len(variable) + negative_index
📝 Summary
Python is easy to learn and use

It is interpreted and dynamically typed

Supports multiple programming paradigms

Widely used in modern technologies