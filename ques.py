##Q1. Check whether a character is a special character
ch = input("Enter a character: ")

if len(ch) == 1:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
        print("Not a Special Character")
    else:
        print("It is a Special Character")
else:
    print("Please enter only one character")
    
####Q2. Reverse a string only if
##starts with uppercase
##ends with digit

##Example: Ravi7 → 7ivaR

name = input("Enter a string: ")

if ('A' <= name[0] <= 'Z') and ('0' <= name[-1] <= '9'):
    rev = ""
    i = len(name) - 1
    while i >= 0:
        rev += name[i]
        i -= 1
    print("Reversed String:", rev)
else:
    print("Condition not satisfied")

    
##Q3. Greatest among 3 numbers
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)
##Q4. Second greatest among 4 numbers (

nums = []

for i in range(4):
    nums.append(int(input("Enter number: ")))

nums = list(set(nums))   # remove duplicates
nums.sort()

print("Second greatest number:", nums[-2])


##Q5. Student result based on percentage
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Absent in Exam")
elif marks < 35:
    print("Fail")
elif marks <= 45:
    print("Average")
elif marks <= 55:
    print("Above Average")
elif marks <= 65:
    print("Medium")
elif marks <= 80:
    print("Good")
elif marks <= 90:
    print("Very Good")
else:
    print("Gold Medal")


##Q6. FIZZ / BUZZ
n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("FIZZ BUZZ")
elif n % 3 == 0:
    print("FIZZ")
elif n % 5 == 0:
    print("BUZZ")
else:
    print("Not divisible by 3 or 5")

    
##Q7. Digit count (single / double / triple)
n = input("Enter a number: ")

length = len(n)

if length == 1:
    print("Single digit")
elif length == 2:
    print("Double digit")
elif length == 3:
    print("Triple digit")
else:
    print("More than 3 digits")

    
##Q8. Quadrant of a point (x, y)
x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x == 0 and y == 0:
    print("Origin")
elif x > 0 and y > 0:
    print("1st Quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
else:
    print("4th Quadrant")

    
##Q9. First 10 even numbers (BEST)
for i in range(0, 20, 2):
    print(i, end=" ")
    
##Q10. First 10 odd numbers
for i in range(1, 20, 2):
    print(i, end=" ")
    
##Q11. First 10 natural numbers
for i in range(1, 11):
    print(i, end=" ")
    
##Q12. First 10 whole numbers
for i in range(0, 11):
    print(i, end=" ")
    
##Q13. Print numbers & their squares
for i in range(1, 11):
    print(i, "→", i*i)
    
##Q14. Sum of first 10 natural numbers
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

##Q15.
##1 1 2 2 ... 10 10

##BEST & CLEAN
for i in range(1, 11):
    print(i, i)
##With formatting (more readable)
for i in range(1, 11):
    print(f"{i} {i}")


    
