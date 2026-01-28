Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#if we use one key more than 1 time then it will override the last value and print the last value
d2={True:33,2:False}
d2
{True: 33, 2: False}
d3={1:33,"a":"Acsa"}
d3
{1: 33, 'a': 'Acsa'}
d3={1:33,"a":"Acsa", 5:43}
type(d3)
<class 'dict'>
d3['a']
'Acsa'
#finding index value of d3
d3[3]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d3[3]
KeyError: 3
d3[5]
43
#finding 2nd index of string in value of the key 'a'
d3['a'][2]
's'
#finding 3rd index of string in value of the key 'a'
d3['a'][3]
'a'
d4 = {1:10, 2:2.25, 2.2:3+22j, 4:False, 'a':{(2.2),(20+2j), 10}, 'b':['Hi',(10)}
      
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
d4 = {1:10, 2:2.25, 2.2:3+22j, 4:False, 'a':{(2.2),(20+2j), 10}, 'b':['Hi',(10)]}
      
d4
      
{1: 10, 2: 2.25, 2.2: (3+22j), 4: False, 'a': {2.2, 10, (20+2j)}, 'b': ['Hi', 10]}
#Here 10 is printed without '()' because here it is not considered as tuple if we write (10,) then it will print (10)
      
#Fetch Hi from dictionary
      
a1 = d4['b']
      
a1[0]
      
'Hi'
#Fetch False from the disctionary
      
d4[4]
      
False
#fetch 2.2 from dictionary
      
#We can’t fetch 2.2 directly because in your dictionary it exists inside a set, and sets in Python are unordered and do not support indexing or positional access.
      
#SLICING
      
#n Python slicing, indexing starts from 0 when moving from left to right. The starting index is inclusive, while the ending index is exclusive, meaning Python slices elements up to end − 1, not end. Therefore, to include the element at position n, the ending index must be n + 1.
      
#In Python, negative slicing works from right to left, where indexing starts at -1 (last element). The starting index is inclusive and the ending index is exclusive, just like positive slicing. Python moves in the direction implied by the indices (right to left), so elements are selected up to end + 1, not including the ending index itself.
      
a = [10, 20, 30, 40, 50]
a[1:4]   # → [20, 30, 40]

SyntaxError: multiple statements found while compiling a single statement
a = [10, 20, 30, 40, 50]
      
a[1:4]   # → [20, 30, 40]
      
[20, 30, 40]
a[-4:-1]   # → [20, 30, 40]
      
[20, 30, 40]

s= 'Dictionary'
      
s[0:3+:1]
      
SyntaxError: invalid syntax
s[::1]     # full string
      
'Dictionary'
s[::-1]    # reverse string
      
'yranoitciD'
s[0:5]     # 'Dicti'
      
'Dicti'
s[-1:-4]
      
''
s[-4:-1]
      
'nar'
s[-1:-4-1:-1]
      
'yran'
s[-1:-4-1:1]
      
''
#To fetch values using negative indexing, we must specify a negative step in slicing, because a negative step tells Python to traverse the sequence from right to left. Without a negative step, Python moves left to right and cannot reach elements using decreasing indices.
      
s2='Dictionary'
      
s2[-1:-10:-2]
      
'yaoti'
s2[-1:-9-1:-2]
      
'yaoti'
s3= ['Hello class', (5.2+2.36j,11, False),{'a':101, 10.1:5500}]
      
#Fetch the reverse of the tuple without skippink any arguements of tuple
      
rev = s3[1][::-1]
      
rev
      
(False, 11, (5.2+2.36j))
by taking both starting and ending index
      
SyntaxError: invalid syntax
s3[1][-1:-4:-1]
      
(False, 11, (5.2+2.36j))
s5=[10,20,(100,200,'Hello"),{1,2,3}] #fetch 200, 400
           
SyntaxError: unterminated string literal (detected at line 1)
s5=[10,20,(100,200,'Hello'),{1,2,3}] #fetch 200, 400
           
s5[2][0]
           
100
s5[2][1]
           
200
#2
           
s6="Hello This is LPU" #fetch 'UPL'
           
s6[-1:-4:-1]
           
'UPL'
s7={'a': ["This is a list"], 'b': [10,20,30,("Hello",'Guys')]}
           
#fetch reverse of guys
           
s7[b][3][2][-1:-5:-1]
           
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s7[b][3][2][-1:-5:-1]
NameError: name 'b' is not defined
s7['b'][3][1][-1:-5:-1]
           
'syuG'
a={2,3,'Tina' ,10+10j}
           
a=(10,5)
           
a={2,3,'Tina' ,10+10j}
           
t=(10,5)
           
result =set.union(t)
           
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    result =set.union(t)
TypeError: descriptor 'union' for 'set' objects doesn't apply to a 'tuple' object
result =a.union(t)
           
result
           
{2, 3, 5, (10+10j), 10, 'Tina'}
result
           
{2, 3, 5, (10+10j), 10, 'Tina'}
set.add(40)
           
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    set.add(40)
TypeError: descriptor 'add' for 'set' objects doesn't apply to a 'int' object
set.add{40}
           
SyntaxError: invalid syntax
a.add(40)
           
a.add((2,22))
           
A
           
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a
           
{2, 3, (10+10j), 40, (2, 22), 'Tina'}
>>> a
...            
{2, 3, (10+10j), 40, (2, 22), 'Tina'}
>>> a.add(("Raju",3))
...            
>>> a
...            
{2, 3, (10+10j), 40, ('Raju', 3), (2, 22), 'Tina'}
>>> a
...            
{2, 3, (10+10j), 40, ('Raju', 3), (2, 22), 'Tina'}
>>> 
>>> #Dictionary
...            
>>> d={1:'Das', 2:4}
...            
>>> d[1]="Alia"
...            
>>> d
...            
{1: 'Alia', 2: 4}
>>> d[7:'Thala']
...            
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    d[7:'Thala']
KeyError: slice(7, 'Thala', None)
>>> d[7]='Thala'
...            
>>> d
...            
{1: 'Alia', 2: 4, 7: 'Thala'}
>>> #Removing elements
...            
>>> d.pop(1)
...            
'Alia'
>>> d
...            
{2: 4, 7: 'Thala'}
