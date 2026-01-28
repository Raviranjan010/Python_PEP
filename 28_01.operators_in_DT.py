Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
[2,3,4]+['Hi']
[2, 3, 4, 'Hi']
#operators
#Arithematic Operator
{2:2,4:5}+{6:7}
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    {2:2,4:5}+{6:7}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
{2:2,4:5}+{2:7}
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    {2:2,4:5}+{2:7}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
{3,44}-{33}
{3, 44}
{100,20}-{"Hello"}
{100, 20}
{100, 20}
{100, 20}
{22,33,4}-{22}
{33, 4}
{22,33,4}-{22,33}
{4}
{22,33,4}-{22,2}
{33, 4}

{22,33,4}-{22,33,4,3}
set()
(3+4j)*3
(9+12j)
(3+4j)**2
(-7+24j)
true/2
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    true/2
NameError: name 'true' is not defined. Did you mean: 'True'?
true%2
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    true%2
NameError: name 'true' is not defined. Did you mean: 'True'?
True/2
0.5
True%2
1
True*2
2
True//2
0

#Logical Operators

Logical and
SyntaxError: invalid syntax
a1=10 and 0
a1
0
'hi' and 'Hello'
'Hello'
'Hello' and 'Hi'
'Hi'
0 and "hi'
SyntaxError: unterminated string literal (detected at line 1)
0 and 'hi'
0
1 and 'hi'
'hi'
{} and 0.0
{}
{2} and 0.0
0.0
{2} and 11
11
\
False and 0j
False
True and 0j
0j
'Hii' and False
False
'Hii' and True
True

0j and False
0j
0j and 2j
0j
0j and True
0j
[] and 22
[]
[22] and 22
22
#if operand 1 is not default value then it will return 2nd operand as output
#if we have any value other then 0/False then 2nd operand will be printed if 1st operand is 0 or False then it will return 0 or False
0 and 0j
0
10 and 3
3
10 and 0
0
"" and 1
''
#or operator
10 or 2
10
\
10 or 0
10
0 or False
False
False or 0
0
"Hi" or "Hello"
'Hi'
#if operand1 value is True then result will Operand1 otherwise we will get operand2 as output
0 or 10
10
10 or 0
10
'hi' or 0
'hi'
>>> 0 or 'hi'
'hi'
>>> {} or 0.0
0.0
>>> {22} or 0.0
{22}
>>> 
>>> 
>>> #Logical Not Operator
>>> not(False)
True
>>> not(0)
True
>>> not("hi")
False
>>> not(True)
False
>>> not(False + True)
False
>>> not(True + False)
False
>>> not(False or True)
False
>>> not('')
True
>>> not(set())
True
>>> #in default value not operator return True always

#RELATIONAL OPERATORS
#Greater than, less than , equals to , not equals to (!=)  greater than or equal to  , less than or equal to (<=)
>>>'Amaan' >'Anshuman'
False
'A'>'a'//check the ascii value

'Amaan' >'Anshuman'
False
'A'>'a'//check the ascii value
SyntaxError: invalid syntax

'Hello'>'Python'
False
'Python'>'Hello'
True
'Python'>'hello'
False
'Hello'>'python'
False

[10,20,30] >[1,2,3]
True
[10,20,30] >[1,30,40]
True
[10,20,30] >[10,20,30]
False
#False because here in both list it will compare the value and here all value are equal so it will
not give true
[10,20,30] >[1,20,40]
True
[1,20,30] >[1,20,40]
False
False because ....

🔍 Comparison Operators in Python (> < ==)
(Strings & Lists – Explained Properly)
Python compares sequences lexicographically (element by element), not by length.

🧵 STRING COMPARISON IN PYTHON
🔹 Core Rules
Strings are compared character by character

Comparison is based on Unicode / ASCII values

Comparison stops at the first different character

Uppercase letters < Lowercase letters

📌 ASCII / Unicode Reference (Important)
Character	ASCII
'A'	65
'Z'	90
'a'	97
'z'	122
👉 Capital letters come before lowercase letters

✅ Examples with Reasons
1️⃣
'Amaan' > 'Anshuman'
Output

False
Reason

'A' == 'A'

'm' (109) vs 'n' (110)

109 < 110 → ❌

2️⃣
'A' > 'a'
❌ SyntaxError because:

//  is NOT a comment in Python
✅ Correct version:

'A' > 'a'   # False
Reason

65 < 97
3️⃣
'Hello' > 'Python'
❌ False

Reason

'H' (72) < 'P' (80)
4️⃣
'Python' > 'Hello'
✅ True

5️⃣
'Python' > 'hello'
❌ False

Reason

'P' (80) < 'h' (104)
6️⃣
'Hello' > 'python'
❌ False

🧠 STRING COMPARISON RULE (One Line)
Strings are compared character-by-character using ASCII/Unicode values.

📦 LIST COMPARISON IN PYTHON
🔹 Core Rules
Lists are compared element by element

First unequal element decides the result

If all elements are equal → result is False for >

Length does NOT matter unless elements are equal

✅ Examples with Reasons
1️⃣
[10, 20, 30] > [1, 2, 3]
✅ True

Reason

10 > 1
2️⃣
[10, 20, 30] > [1, 30, 40]
✅ True

Reason

10 > 1
3️⃣
[10, 20, 30] > [10, 20, 30]
❌ False

Reason

All elements equal

No element is greater

4️⃣
[10, 20, 30] > [1, 20, 40]
✅ True

Reason

10 > 1
5️⃣
[1, 20, 30] > [1, 20, 40]
❌ False

Reason

1 == 1

20 == 20

30 < 40

🧠 LIST COMPARISON RULE (One Line)
Python compares lists element-by-element and stops at the first difference.

⚠️ Common Mistakes
❌ Thinking length matters first
❌ Thinking all elements are compared
❌ Confusing ASCII with alphabet order
❌ Using // instead of # for comments

✅ Final Summary Table
Comparison Type	Rule
String vs String	ASCII / Unicode
List vs List	Element-by-element
Upper vs Lower	Uppercase is smaller
Equal sequences	> returns False


>>>

>>>

>>>

>>>

>>>

>>>

>>>

>>>

>>>

{1,3,4,5}>{1,2,3}
False
{1,3,4,5}>{1,5,3}
True
#it will return true all elements of 2nd op must be present in first set
{3}>[3]
Traceback (most recent call last) :
File "<pyshell#21>", line 1, in <module>
{3}>[3]
TypeError: '>' not supported between instances of 'set' and 'list'
[3]>{3}
Traceback (most recent call last) :
File "<pyshell#22>", line 1, in <module>
[3]>{3}
TypeError: '>' not supported between instances of 'list' and 'set'
[3]>[3]
False
[3]>[5]
False
[7]>[5]
True
[7,4,5]>[5,3,2]
True
[5,3,2]>[7,4,5]
KeyboardInterrupt
[5,3,2]>[7,4,5]


'22' >'Raj'
False
'Raj'>'22'
True
22>[22]
Traceback (most recent call last) :
File "<pyshell#32>", line 1, in <module>
22>[22]
TypeError: '>' not supported between instances of 'int' and 'list'
[22]>22
Traceback (most recent call last) :
File "<pyshell#33>", line 1, in <module>
[22]>22
TypeError: '>' not supported between instances of 'list' and 'int'
'Raj'>22
Traceback (most recent call last) :
File "<pyshell#34>", line 1, in <module>
'Raj'>22
TypeError: '>' not supported between instances of 'str' and 'int'
ord ('d')>3
True
ord('d')<3
False
ord ('d')
100




