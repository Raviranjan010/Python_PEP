Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a='23.3'
int(a)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: '23.3'
L=[1,2,3]
a=l.copy()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a=l.copy()
NameError: name 'l' is not defined. Did you mean: 'L'?
L=[1,2,3]
a=L.copy()
a[2]=23
l
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l
NameError: name 'l' is not defined. Did you mean: 'L'?
L
[1, 2, 3]
a
[1, 2, 23]
l2=[1,2,3,[2,3,2],7]
l3=l2[3]
l3
[2, 3, 2]
l4=l3.copy()
l4[2]=2
l4
[2, 3, 2]
l2
[1, 2, 3, [2, 3, 2], 7]
l4[2]=99
>>> l1
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l1
NameError: name 'l1' is not defined. Did you mean: 'l2'?
>>> l2
[1, 2, 3, [2, 3, 2], 7]
>>> l4
[2, 3, 99]
>>> l3
[2, 3, 2]
>>> #General copy
>>> ## also known as normal and reference
>>> #it is for list only
>>> ####it pointing to the same memory
>>> 
>>> #Shallow copy
>>> #using  l.copy()
\
>>> #it content value space create content of value space and create new memory layer
>>> inside nested list not affect the both values
SyntaxError: invalid syntax
>>> 
>>> #deep copy operation
>>> 
>>> import copy
>>> #var=copy.deepcopy(source_var)
>>> # does not copy variable space and valuespace
>>> 
>>> import copy
>>> l=[1,2,33,4,7]
>>> y=copy.deepcopy(l)
>>> y
[1, 2, 33, 4, 7]
>>> l[3]=77
>>> l
[1, 2, 33, 77, 7]
>>> y
[1, 2, 33, 4, 7]
>>> #in this both become independent
