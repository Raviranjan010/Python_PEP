


a=input("enter : ")
if type(a)==int:
    if a==a[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
else:
    print("Enter a valid number")
