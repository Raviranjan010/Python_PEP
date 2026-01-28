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
