Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="Ram"

a
'Ram'
b=''raj''
SyntaxError: invalid syntax. Is this intended to be part of the string?
>>> c='raj'
>>> c
'raj'
>>> d = "Raj's car"
>>> d
"Raj's car"
>>> s='python
SyntaxError: unterminated string literal (detected at line 1)
>>> s='python'
>>> s[-5]
'y'
>>> s1 = 'This is python class'
>>> s1[-11]
'y'
>>> l2=[10,"Python_class"]
>>> s=l2[1]
>>> s3=s[7]
>>> 
>>> s3
'c'
>>> s4=s[6]
>>> s4
'_'
>>> l4=[10,"Python_class"]
>>> s5=l4[1][6]
>>> s5
'_'
>>> l6=[1-,2.2,[2+2j, True,['Yadav ji','Pandey Ji' False]]]
SyntaxError: invalid syntax
>>> l6=[1,2.2,[2+2j, True,['Yadav ji','Pandey Ji' False]]]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> l6=[1,2.2,[2+2j, True,['Yadav ji','Pandey Ji' ,False]]]
>>> l6[2][2]
['Yadav ji', 'Pandey Ji', False]
>>> l6[2][2][0]
'Yadav ji'
>>> l6[2][2][1]
'Pandey Ji'
>>> l6[-1][-1][1]
'Pandey Ji'
