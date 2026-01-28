Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
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
#False because here in both list it will compare the value and here all value are equal so it will not give true
[10,20,30] >[1,20,40]
True
[1,20,30] >[1,20,40]
False
False because ....
SyntaxError: invalid syntax


{1,3,4,5}>{1,2,3}
False
{1,3,4,5}>{1,5,3}
True
#it will return true all elements of 2nd op must be present in first set
{3}>[3]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    {3}>[3]
TypeError: '>' not supported between instances of 'set' and 'list'
[3]>{3}
Traceback (most recent call last):
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
False
False
False

'22'>'Raj'
False
'Raj'>'22'
True
22>[22]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    22>[22]
TypeError: '>' not supported between instances of 'int' and 'list'
[22]>22
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    [22]>22
TypeError: '>' not supported between instances of 'list' and 'int'
'Raj'>22
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    'Raj'>22
TypeError: '>' not supported between instances of 'str' and 'int'
ord('d')>3
True
ord('d')<3
False
ord('d')
100
1==1.0+0jj
SyntaxError: invalid imaginary literal
1==1.0+0j
True
1.0+0j==1
True
10==(10)
True
10==(10,)
False
#(10) is just an integer because parentheses only group values, but (10,) is a tuple because the comma creates a tuple—so 10 == (10) is True, while 10 == (10,) is False.

[10]!=10.0
True
10!=10.0
False
#[10] != 10.0 is True because a list and a float are different data types and Python never considers them equal, but 10 != 10.0 is False because Python compares their numeric values (10 == 10.0) and they are equal.
bbbbbbbbbbb
KeyboardInterrupt
[10,20,30] >=[10,20,30]
True
#If two lists are exactly equal, >= and <= both return True.

{2,3,44}>{2,3,44}
False
{2,3,44}={2,3,44}
SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?
{2,3,44}>={2,3,44}
True
{2,3,44}=={2,3,44}
True
{2,3,44}=={2,3,44,3}
True
{2,3,44}=={2,3,44,33}
False
{2,3,44,33}=={2,3,44}
False
{2,3,44,33}>={2,3,44}
True
{2,3,44}=<{2,3,44,33}
SyntaxError: cannot assign to set display
{2,3,44}<={2,3,44,33}
True
True==False
False
False==False
True
False==True
False
{}<={}
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    {}<={}
TypeError: '<=' not supported between instances of 'dict' and 'dict'
[]<=[]
True
[2]<=[]
False
[2]<=[3]
True
(2,)<=[3]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    (2,)<=[3]
TypeError: '<=' not supported between instances of 'tuple' and 'list'
>>> g]
SyntaxError: unmatched ']'
>>> a=21
>>> a+=a
>>> a
42
>>> #MEMBERSHIP OPERATORS
>>> 10 in [10,20,30]
True
>>> 1 in [10,20,30]
False
>>> 1 in {10,20,30}
False
>>> 1 not in {10,20,30}
True
>>> 
>>> 
>>> #IDENTITY Operators
>>> #is and is not
>>> a=10
>>> b=20
>>> c=10
>>> a is c
True
>>> a is b
False
>>> a is not b
True
