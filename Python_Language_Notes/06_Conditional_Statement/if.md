'''a=int(input("Enter a number TO Check weather a number is +ve or -ve: "))
if(a>0):
    print("Positive")
if(a<0):
    print("Negative")
if(a==0):
    print("It's 0")
    
#Check weather a mumber is even or odd
b=int(input("Enter a number to check even or odd: "))
if(b%2==0):
    print("Number is Even")
else:
    print("Number is odd")


#Take any number as age and check weather that age is elegible for vite or not
c=int(input("Enter age elegible for vote: "))
if(c>=18):
    print("Elegible for vote")
else:
    print("Not elegible for vote")



#Take 5 different variable and store marks: maths ,science,eng,Social science subjects and calculate it's avearage and find out the student is pass or fail
a1=int(input("Enter marks of maths: "))
a2=int(input("Enter marks of Science: "))
a3=int(input("Enter marks of English: "))
a4=int(input("Enter marks of Hindi: "))
a5=int(input("Enter marks of Social Science: "))

avg=(a1+a2+a3+a4+a5)/5
print(avg)
if(avg>=35):
    print("Pass")
else:
    print("Fail")



#Example of if ,elif and else
#b1=

#Take a user input a number between 1 to 7 and on the basis of the number tell which day it is indicating
    
c1=int(input("Enter a value to check day: "))
if(C1==1):
       print("Monday")
elif(C1==2):
       print("Tuesday")
elif(C1==3):
       print("Wednesday")
elif(C1==4):
       print("Thrusday")
elif(C1==5):
       print("Friday")
elif(C1==6):
       print("Saturday")
elif(C1==7):
       print("Sunday")
else:
       print("Enter a valid number")


#Predict the status of student result based on the obtained result using nested if

marks = int(input("Enter obtained marks: "))

if marks >= 40:
    if marks >= 75:
        print("Result: Distinction")
    else:
        if marks >= 60:
            print("Result: First Class")
        else:
            if marks >= 50:
                print("Result: Second Class")
            else:
                print("Result: Pass")
else:
    print("Result: Fail")'''


#check weather elegible for vote or not on the basis of age , voter id , alive use of nested if 
          
age = int(input("Enter your age: "))

if age >= 18:
    voter_id = input("voter ID hai? (yes/no): ")

    if voter_id == "yes":
        Jinda_hai = input("Jinda ho?(yes/no): ")

        if Jinda_hai == "yes":
            print("Eligible haii")
        else:
            print("Not eligible (Person Jinda nahi hai)")
    else:
        print("Not eligible (voter ID le kar aao)")
else:
    print("Not eligible ,age kam hai)")

