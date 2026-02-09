
# Introduction to Python

## What is Python?
Python is a **high-level, interpreted, general-purpose programming language** designed with an emphasis on **code readability and simplicity**. It enables programmers to write clear, logical code for both small scripts and large-scale applications.

History of Python
*   Developed by **Guido van Rossum**.
*   First released in **1991**.
*   Named after the British comedy group **“Monty Python’s Flying Circus”** (not the snake).
*   Designed as a successor to the ABC language.

Why Python Was Created
Python was designed to:
*   Reduce the complexity of programming.
*   Increase developer productivity.
*   Allow beginners to learn programming easily.
*   Support multiple programming paradigms.

Key Features of Python
1. Simple and Easy to Learn
Uses English-like syntax

Fewer lines of code compared to C/C++/Java

*   **Simple and Easy to Learn**: Uses English-like syntax, requiring fewer lines of code compared to languages like C/C++/Java.
*   **High-Level Language**: Abstracts away complex hardware details, allowing programmers to focus on logic rather than manual memory management.
*   **Interpreted Language**: Executes code line by line, which means no separate compilation step and often easier debugging.
*   **Dynamically Typed**: Variable types are decided at runtime; there's no need to declare them explicitly.
*   **Object-Oriented**: Supports classes and objects, promoting code reusability and modularity.
*   **Open Source and Free**: Free to use and distribute, benefiting from a large and active community.
*   **Portable (Platform-Independent)**: The same code can run on various operating systems like Windows, Linux, and macOS without modification.
*   **Extensive Standard Library**: Comes with a rich set of built-in modules for tasks such as:
    *   File handling
    *   Mathematical operations
    *   Date & time manipulation
    *   Operating system interactions
    *   Networking
*   **Supports Multiple Programming Paradigms**: Accommodates procedural, object-oriented, and functional programming styles.
*   **User-Defined Libraries**: Allows developers to create, define, and share their own custom functions and libraries.

Applications of Python
Python is used in almost every domain:

Web Development (Django, Flask)

Data Science & Analytics

Artificial Intelligence & Machine Learning

Automation & Scripting

Game Development

Desktop Applications

Cybersecurity

Internet of Things (IoT)

Python Programming Paradigms
Python supports:
*   Procedural Programming
*   Object-Oriented Programming
*   Functional Programming

Python Versions
Python 2.x → Discontinued (No longer supported)

Python 3.x → Current and recommended version

Advantages of Python
*   Easy and readable syntax.
*   Faster development cycles.
*   Huge and diverse library ecosystem.
*   Cross-platform compatibility.
*   Strong community support.

Limitations of Python
*   Generally slower than compiled languages.
*   Not always ideal for memory-intensive tasks.
*   Limited native support for mobile application development.

Python Program Structure
A basic Python program includes:

Statements

Indentation instead of braces { }

Comments using #

Example:

print("Hello, World!")
Important Characteristics
Case-sensitive language

Indentation is mandatory

No semicolon required

Supports interactive mode

Conclusion
Python is a powerful, flexible, and beginner-friendly language widely used in modern technology fields.
Its simplicity, readability, and versatility make it one of the most popular programming languages today.

father of python is Guido van Rossum.
he got name of python by his circus -Monty python's fling circus 

Python – Uses, Features, and Basic Components
Python is Used In
Python is widely used in many modern technology fields such as:

Game Development

Desktop Applications

Cybersecurity

Mobile Application Development

Web Development

Cloud Computing

Generative Artificial Intelligence

Data Analysis

Scientific Research

Software Companies / IT Industry

Because of its simplicity and powerful libraries, Python is suitable for both small programs and large enterprise applications.

Features of Python
1. Easy to Use
Python syntax is simple and readable

Suitable for beginners and professionals

2. Dynamically Typed Language
No need to declare data types

Variable type is decided at runtime

Example:

x = 10
x = "Python"
3. Interpreter-Based Language
Python code is executed line by line

Errors are shown immediately, making debugging easy

4. Huge Number of Library Functions
Python has a large standard library

Libraries are available for:

Math

File handling

Web development

Data science

AI and ML

5. Platform Independent
Same Python program can run on:

Windows

Linux

macOS

No need to modify code for different systems

6. High-Level Programming Language
No need to manage memory

Focus is on problem-solving rather than hardware details

7. Supports Multiple Programming Paradigms
Python supports:

Procedural programming (with functions)

Object-Oriented programming (with classes)

Functional programming

You can write programs:

With functions or without functions

With classes or without classes

8. Open Source and Free
Python is free to use

Source code is publicly available

Anyone can modify and improve it

9. User-Defined Libraries
Any programmer can:

Create their own library

Define custom functions

Share libraries with others

Developers can suggest changes to improve libraries

Basic Components of Python
1. Library Functions
Predefined functions provided by Python libraries

Help perform tasks easily

Examples:

math.sqrt()

random.randint()

os.getcwd()

2. Keywords
Reserved words with special meaning

Cannot be used as variable names

Examples:

if, else, for, while, break, continue, True, False
3. Operators
Operators are symbols used to perform operations.

Types of operators:

Arithmetic (+, -, *, /)

Relational (>, <, ==)

Logical (and, or, not)

Assignment (=, +=)

Membership (in, not in)

4. Built-in (Inbuilt) Functions
Functions already available in Python

No need to import any module

Examples:

print()
len()
type()
input()
range()
Conclusion
Python is a powerful, flexible, and user-friendly language used in almost every modern technology domain.
Its features like dynamic typing, platform independence, huge libraries, and multi-paradigm support make it one of the most popular programming languages today.

Operators in Python (Easy Way to Remember)
👉 Mnemonic: A L A R M B I

Letter	Operator Type	Description
A	Algorithmic (Arithmetic)	Used for mathematical operations
L	Logical	Used for logical conditions
A	Assignment	Used to assign values
R	Relational	Used for comparison
M	Membership	Used to check membership
B	Bitwise	Used for bit-level operations
I	Identity	Used to compare memory location
1. Algorithmic (Arithmetic) Operators
+ - * / % // **

Example:

a = 10
b = 3
print(a + b)
2. Logical Operators
and, or, not

Example:

a = True
b = False
print(a and b)
3. Assignment Operators
=, +=, -=, *=, /=

Example:

a = 10
a += 5
4. Relational Operators
>, <, >=, <=, ==, !=

Example:

print(10 > 5)
5. Membership Operators
in, not in

Example:

print('a' in 'apple')
6. Bitwise Operators
&, |, ^, ~, <<, >>

Example:

print(5 & 3)
7. Identity Operators
is, is not

Example:

a = 10
b = 10
print(a is b)
Inbuilt (Built-in) Functions
1. type()
👉 Used to find the type of data

a = 10
print(type(a))
2. id()
👉 Used to find the memory address (identity) of an object

a = 10
print(id(a))
3. len()
👉 Used to find the length of data like string, list, tuple, etc.

name = "Python"
print(len(name))
Variable Space and Value Space
Variable Space	Value Space
Variable name is stored	Actual value is stored
Example:

a = 100
Explanation:

a → stored in variable space

100 → stored in value space

Both may point to the same memory address

Illustration:

a  -------->  100
0x11         0x11 [100]
Multiple Variable Creation
Python allows creating multiple variables in one line.

Example:
a, b, c = 10, 20, 30
Same value:

x = y = z = 5
Identifiers
👉 An identifier is the name given to a variable, function, or class.

Example:

a = 10
Here, a is an identifier.

Rules of Identifiers
Identifier should not be a keyword

No space allowed in identifier

Should not start with a number

Only underscore (_) is allowed as a special character

Identifiers are case-sensitive

age and Age are different

Can be alphanumeric

Length should not exceed 72 characters

Valid:

total_marks = 90
Invalid:

2value = 10
my value = 5
Data Types in Python
1. Single Value / Individual Data Types
Stores only one value

Examples:

int → 10

float → 3.14

complex → 2+3j

bool → True

2. Multi-Value Data Types
Stores multiple values

Examples:

list → [1, 2, 3]

tuple → (1, 2, 3)

set → {1, 2, 3}

string → "Python"

dictionary → {"a": 1}
