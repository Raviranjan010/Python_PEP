c=31
def school():
    a=30
    b=23
    c=a+b
    def Class():
        global c
        print(c)
        c=7
    Class()
    
school()





##Your Code (Original)
##c = 31
##
##def school():
##    a = 30
##    b = 23
##    c = a + b
##
##    def Class():
##        global c
##        print(c)
##        c = 7
##
##    Class()
##
####school()
##1️⃣ MAIN MISTAKE (Why there is NO OUTPUT)
##❌ You commented out the function call
####school()
##👉 Because school() is never executed, nothing runs → no output.
##
##✅ Fix
##school()
##2️⃣ WHAT HAPPENS AFTER FIXING THE CALL
##Execution flow (important):
##Global c = 31
##
##school() is called
##
##Inside school():
##
##a = 30, b = 23
##
##c = a + b → this c is LOCAL to school()
##
##Class() is called
##
##Inside Class():
##
##global c → refers to GLOBAL c, not school’s c
##
##print(c) → prints 31
##
##c = 7 → modifies GLOBAL c
##
##✅ OUTPUT
##31
##Global c after execution:
##c == 7
##3️⃣ WHY c = a + b IS IGNORED
##This line:
##
##c = a + b
##❗ Creates a LOCAL variable inside school()
##
##But Class() uses:
##
##global c
##So:
##
##Class() ❌ cannot see school()’s c
##
##It ONLY sees global c
##
##4️⃣ CASE THAT WILL GIVE AN ERROR (VERY IMPORTANT)
##❌ If global c does NOT exist
##def school():
##    def Class():
##        global c
##        print(c)
##    Class()
##
##school()
##❌ ERROR:
##NameError: name 'c' is not defined
##📌 Because:
##
##global c tells Python to look in global scope
##
##But c does not exist globally
##
##5️⃣ WRONG EXPECTATION CASE (Common Student Mistake)
##❌ Expecting output = 53
##c = 31
##school()
##Student thinks:
##
##30 + 23 = 53
##❌ Wrong, because:
##
##Class() does NOT access school()’s c
##
##global c ignores local variables
##
##6️⃣ CORRECT WAY TO ACCESS school()’s c (NO ERROR)
##✅ Use nonlocal
##c = 31
##
##def school():
##    a = 30
##    b = 23
##    c = a + b
##
##    def Class():
##        nonlocal c
##        print(c)
##        c = 7
##
##    Class()
##
##school()
##✅ OUTPUT
##53
##7️⃣ global vs nonlocal (EXAM GOLD POINT)
##Keyword	Accesses
##global	Global variable
##nonlocal	Nearest enclosing function variable
##8️⃣ FINAL SUMMARY (Exam Ready)
##Why no output?
##school() was not called
##
##Why 31 is printed?
##global c refers to global c
##
##Why no error in your code?
##Global c exists before Class() runs
##
##When error occurs?
##If global c is used but c is NOT defined globally

## write a program to define a function which would give factorial of a number 

##
##def fac(n):
##    f=1
##    for i in range(1,n+1):
##        f*=i
##    return f
##num=int(input("Enter a  number: "))
##print(fac(num))
##
####
##def f_name(a):
##    print(a)
##f_name(2,3,44)
###it will give error because here only 1 parameter initialized



def f_name(*a):
    print(a)
    print(type(a))
f_name(2,3,44)
#type(a) 
#list(a)
 #we can use single packing using astriskfor  multiple values in this format and we will get tuple as output

def f_name(*a):
    print(a)
f_name()




###Each and every character as input value print must be inside tuple () in character format
##in ('p','y','t','h','o','n')
##DIRECT & CORRECT SOLUTION

def char_tuple(s):
    return tuple(s)

print(char_tuple("python"))

##
####USING FUNCTION (With Argument)
##
##s = input("Enter a string: ")
##t = ()
##
##for ch in s:
##    t = t + (ch,)
##
##print(t)


##def char():
##    s = input("Enter a string: ")
##    for ch in s:
##        print(tup(ch))
##
##char()
##

##to taking input for dictionary
##def f_name(**a):
##    print(a)
##    print(type(a))
####f_name(var=value,var2=value2....)
##
##def f_name(**a):
##    print(a)
##    print(type(a))
##
##f_name(a=12, b=25, c=40)
####TAKING DICTIONARY INPUT FROM USER (USING LOOP)
##
##d = {}
##
##n = int(input("Enter number of key-value pairs: "))
##
##for i in range(n):
##    key = input("Enter key: ")
##    value = input("Enter value: ")
##    d[key] = value
##
##print(d)
##print(type(d))



##keyword arguement is passing key and value in parameters in function
## eg f_name(var=value,val=value)


def f_name(*a,**b):##we have to keep tuple arguements after normal one
    print(a,b)
    print(type(a))
    print(type(b))
f_name(2,3,44,a=3,b=2,c=55)


##🔹 PACKING vs UNPACKING (Quick Recall)
##Concept	Meaning
##Packing	Collecting multiple values into one variable
##Unpacking	Splitting values from tuple/list/dict into variables
##✅ 1️⃣ UNPACKING A TUPLE
def unpack(a, b, c):
    print(a, b, c)

unpack(*(12, 2, 32))

##✅ 2️⃣ UNPACKING A LIST
def unpack(a, b, c):
    print(a, b, c)

unpack(*[10, 20, 30])
##✅ 3️⃣ UNPACKING A SET (ORDER NOT GUARANTEED ⚠️)
def unpack(a, b, c):
    print(a, b, c)

unpack(*{1, 2, 3})
##⚠️ Order may change.
##
##✅ 4️⃣ UNPACKING A STRING
def unpack(a, b, c):
    print(a, b, c)

unpack(*"abc")



##❌ 5️⃣ ERROR CASE – VALUE COUNT MISMATCH
##unpack(*(1, 2))
##❌ Error
##TypeError: unpack() missing 1 required positional argument
##❌ 6️⃣ ERROR CASE – TOO MANY VALUES
##unpack(*(1, 2, 3, 4))
##❌ Error
##TypeError: unpack() takes 3 positional arguments but 4 were given
##✅ 7️⃣ PACKING USING *args
def pack(*a):
    print(a)
    print(type(a))

pack(1, 2, 3, 4)

##✅ 8️⃣ PACKING + UNPACKING TOGETHER
def mix(a, b, *c):
    print(a)
    print(b)
    print(c)

mix(1, 2, 3, 4, 5)

##✅ 9️⃣ UNPACKING DICTIONARY VALUES
def unpack(a, b):
    print(a, b)

d = {'a': 10, 'b': 20}
unpack(**d)
##📌 Keys must match parameter names.
##
####❌ 10️⃣ ERROR CASE – KEY MISMATCH IN DICT UNPACKING
##d = {'x': 1, 'y': 2}
##unpack(**d)
##❌ Error
##TypeError: unpack() got an unexpected keyword argument 'x'



##✅ 1️⃣1️⃣ UNPACKING WITH DEFAULT VALUES
def unpack(a, b, c=0):
    print(a, b, c)

unpack(*(1, 2))

##first we have to take positional arguements before default arguements because it is 




# 1. Positional Arguments
# Values are passed in order
def add(a, b):
    print(a + b)

add(10, 20)
# -------------------------------
# 2. Keyword Arguments
# Values are passed using parameter names
def student(name, age):
    print(name, age)

student(age=20, name="Ravi")
# -------------------------------
# 3. Default Arguments
# Default value is used if no value is passed
def greet(name="User"):
    print("Hello", name)

greet()
greet("Ravi")
# -------------------------------
# 4. Variable Length Arguments (*args)
# Packs multiple values into a tuple
def total(*numbers):
    print(numbers)

total(1, 2, 3, 4)
# -------------------------------
# 5. Keyword Variable Length Arguments (**kwargs)
# Packs keyword arguments into a dictionary
def details(**info):
    print(info)

details(name="Ravi", age=20, city="Delhi")
# -------------------------------
# 6. Combination of Arguments
# Normal + *args
def demo(a, b, *c):
    print(a)
    print(b)
    print(c)

demo(1, 2, 3, 4, 5)
# -------------------------------
# 7. Positional Unpacking
# Tuple values unpacked using *
def show(a, b, c):
    print(a, b, c)

show(*(10, 20, 30))
# -------------------------------
# 8. Keyword Unpacking
# Dictionary values unpacked using **
def show(a, b):
    print(a, b)

d = {"a": 5, "b": 10}
show(**d)
# -------------------------------
# 9. Error Case: Too few arguments
# Missing required arguments
def test(a, b):
    print(a, b)

# test(10)   # TypeError
# -------------------------------
# 10. Error Case: Too many arguments
def test(a, b):
    print(a, b)

# test(1, 2, 3)   # TypeError


# -------------------------------
# POSitional Arguments
# Values are passed to parameters based on their position
# Order of values is important

def add(a, b):
    print(a + b)

add(10, 20)
# Output: 30
# -------------------------------
# DEFAULT Arguments
# Default value is used when no argument is passed
# If value is passed, it overrides the default

def greet(name="User"):
    print("Hello", name)

greet()
# Output: Hello User

greet("Ravi")
# Output: Hello Ravi
# -------------------------------
# POSitional + DEFAULT Arguments together
# Default arguments must be placed after positional arguments

def student(name, age=18):
    print(name, age)

student("Ravi")
# Output: Ravi 18

student("Ravi", 20)
# Output: Ravi 20
# -------------------------------
# ERROR CASE
# Default argument cannot come before positional argument

# def demo(a=10, b):
#     print(a, b)
# SyntaxError
# -------------------------------
# IMPORTANT RULE
# Positional arguments are matched first
# Default values are used only if argument is missing
