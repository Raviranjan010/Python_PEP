##def add():
##    a = int(input("Enter 1st number: "))
##    b = int(input("Enter 2nd number: "))
##    sum=a+b
##    return sum
##
##print("Sum =", add())


###create a func to which will extract string from a list only if the string is palindrome string
##def e(l):
##    res = []
##    
##    for i in l:
##        if type(i)==str:
##            if i== i[::-1]:
##                res.append(i)
##                
##    return res
##
##print(e(["madam", "hello", "level", 12321, "radar", "python", "noon"]))
##



####def e(lst):
####    return [s for s in lst if s == s[::-1]]
##def e(l):
##    res = []
##    
##    for i in l:
##        if type(i)==str:
##            if i== i[::-1]:
##                res.append(i)
##    print(res)
##
##data = ["madam", "hello", "level", 123, "radar", "python", "noon"]
##
##e(data)
##
###Write a program to create a function to concatinate 2 list values without using '+' operator
##
#### Method 1 using extend keyword
##def con(l1, l2):
##    l1.extend(l2)
##    print("Concatenated List:", l1)
##list1 = [1, 2, 3]
##list2 = [4, 5, 6]
##
##con(list1, list2)
##
#### Method 2
##def con2(l1, l2):
##    for i in l2:
##        l1.append(i)
##    print("Concatenated List:", l1)
##
##
##list1 = ['a', 'b','c']
##list2 = ['h','d','k']
##
##con2(list1, list2)


def con(l1,l2):
    out= l1
    for i in l2:
        out.append(i)
    print(out)
    
con(eval(input()),eval(input()))


