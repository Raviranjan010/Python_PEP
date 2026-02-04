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
