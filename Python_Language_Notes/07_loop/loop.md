#take user input as character , and check weather a given character is a special character is a special or not
#2.Write a proram to print reverse of string if it is starting with uppercase alphabet and ending with digit

#3.write a program to find the greatest of three number taken as user input
#4.write a program to find the second greatest among 4 numbers
#5.predict the status of student result based on the obtained percentage as a user input
#6.take x and y variable,as of quadrant values and check x and y lies in which particular quadrant
#7.take a user input and check is the number is single digit ,double digit ,triple digit or more then  digit number
#8. take integer as input print FIZZ





#loop

#while loop
#initialization of loop var
###while condition:
###    .....
###    update looping variable
##
##a=input("Enter some value: ")
##i=1
##while(i<=5):
##    print(a)
##    i+=1
##    
##
###print natural number
##a1=int(input("Enter a number: "))
##i=1
##while i<=a1:
##       print(i,end="")
##       i+=1
       



#write a program to print even number from 1 to 50
#a2=int(input("Enter a number")
##i=0
##while(i<=50):
##       if(i%2==0):
##           print(i,end=" ")
##           i+=2
##
##
##
###Write a program to reverse the reverse of a number
##vnum = int(input("Enter a number: "))
##
### First reverse
##rev1 = 0
##temp = num
##while temp > 0:
##    rev1 = rev1 * 10 + temp % 10
##    temp //= 10
##rev2 = 0
##temp = rev1
##while temp > 0:
##    rev2 = rev2 * 10 + temp % 10
##    temp //= 10
##
##print("Original number:", num)
##print("After first reverse:", rev1)
##print("After reversing again:", rev2)
##
n = int(input("Enter num: "))
rev=0
while (n>0):
    lastDig=n%10
    rev = rev * 10 +lastDig
    n = n // 10
print(rev)
    

       
#1) Check whether a character is a special character
ch = input("Enter a character: ")

if not ch.isalnum():
    print("Special Character")
else:
    print("Not a Special Character")
#2) Reverse string if it starts with uppercase and ends with digit
s = input("Enter a string: ")

if s[0].isupper() and s[-1].isdigit():
    print(s[::-1])
else:
    print("Condition not satisfied")
#3) Find the greatest among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)
#4) Find the second greatest among four numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))

nums = [a, b, c, d]
nums.sort()

print("Second Greatest:", nums[-2])
#5) Predict student result based on percentage
p = float(input("Enter percentage: "))

if p >= 90:
    print("Grade: A+")
elif p >= 75:
    print("Grade: A")
elif p >= 60:
    print("Grade: B")
elif p >= 40:
    print("Grade: C")
else:
    print("Fail")
#6) Check which quadrant (x, y) lies in
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

if x > 0 and y > 0:
    print("First Quadrant")
elif x < 0 and y > 0:
    print("Second Quadrant")
elif x < 0 and y < 0:
    print("Third Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
else:
    print("On Axis")
#7) Check number of digits
n = abs(int(input("Enter a number: ")))

if n < 10:
    print("Single Digit")
elif n < 100:
    print("Double Digit")
elif n < 1000:
    print("Triple Digit")
else:
    print("More than 3 digits")
#8) FIZZ / BUZZ / FIZZBUZZ
n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("FIZZBUZZ")
elif n % 3 == 0:
    print("FIZZ")
elif n % 5 == 0:
    print("BUZZ")
else:
    print("Not divisible by 3 or 5")



#for loop
##for var in collection/sequence:
s=[2,3,5,8]
sum=0
for i in s:
    sum+=i
print(sum)


#i can traverse in dict,list ,string and tuple

s2="POWER-BI"

for i in s2:
    print(i)
    


s3="This is Python Class"
#print reverse
rev=""
for i in s3:
    rev=i+rev
print(rev)


#write a program to find the length of given collection without len keyword
##s3 = [10, 20, 30, 40, 50]

count = 0
for i in s3:
    count += 1

print(count)


#write a program to replace space with underscore in given string

s3 = "This is Python Class"
result = ""

for i in s3:
    if i == " ":
        result += "_"
    else:
        result += i
print(result)



#take a list and pass duplicate values and remove the duplicate value from the list using for loop
l = [2, 5, 4, 3, 4, 7, 7]
u = []

for i in l:
    if i not in u:   
        u.append(i)
print(u)

#input: [10,(3+4j),'hi',(10,20),'hello',False,'Python']
#output: {'hi':2,'hello':5,'python':6}

data = [10,(3+4j),'hi',(10, 20),'hello',False,'Python']

res = {}
for i in data:
    if type(i) == str:
        res[i] = len(i)

print(res)

# ← membership operator

##s4=set(l)
##print(s4)
##l2=list(s4)
##print(l2)

#printing reverse of natural number up from 10 to 1
print("printing 1st 10 natural number in reverse using while loop")
i = 10

while i >= 1:
    print(i)
    i -= 1
print("\n")
print("printing 1st 10 whole number in reverse using while loop")
i = 10

while i >= 0:
    print(i)
    i -= 1
print("\n")


#using for loop
print("printing 1st 10 natural number in reverse using for loop")
for i in range(1,11,-1):
    print(i)

#using for loop
print("natural number between 1 and 10 using for loop using while loop")
for i in range(1,10):
    print(i)
print("\n")




#using while loop
print("even number between 1 and 10 using while loop")
i = 1

while i < 10:
    if i % 2 == 0:
        print(i)
    i += 1
print("\n")


#First 10 even numbers

print("first 10 even numbers")
count = 0
i = 0

while count < 10:
    if i % 2 == 0:
        print(i)
        count += 1
    i += 1

#multiple of 10 upto 300
for i in range(1 ,300):
    if(i%10==0):
        print(i)


#multiple of 10 upto 300 in reverse order
for i in range(300,1,-1):
    if(i%10==0):
        print(i,end=" ")

print("\n")

#multiple of 10 upto 300 in reverse order using while loop

i>300
while i>=10:
    print(i,end=" ")
    i-=10



#input:['Hello','This','is','Python','Class']
#output: {'Hello':'olleH','This':'sihT','is':'si','Python':'nohtyP','Class':'ssalC'}
    
#without slicing 
##l =['Hello','This', 'is', 'Python', 'Class']
##res = {}
##
##for s in l:
##    rev = ""
##    i = len(s)-1
##    while i >= 0:
##        rev += s[i]
##        i -= 1
##    result[s] = rev
##
##print(res)


l = ['Hello', 'This', 'is', 'Python', 'Class']
res = {}

for s in l:
    rev = ""
    i = len(s) - 1
    while i >= 0:
        rev += s[i]
        i -= 1
    res[s] = rev

print(res)


