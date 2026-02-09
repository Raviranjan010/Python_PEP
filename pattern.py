n = 4

for i in range(n):          # Rows
    for j in range(n):      # Columns
        print("*", end=" ")
    print()                 # New line after each row
            

for i in range(1,20):
    print(i)
    if(i==9):
##        print(i)
        break


##ask for user input from user until he enter correct and matching "LPU@123" Unless ask for repeating
Pass = "LPU@123"

while True:
    user =input("Enter password: ")
    
    if user == Pass:
        print("Sahi kaha aapne")
        break
    else:
        print("Galat hai be!")


C_Pass = "LPU@123"
C_user="Ravi"

while True:
    user =input("Enter User Name: ")
    Pass =input("Enter password: ")
    
    if user == C_user and Pass==C_Pass:
        print("Sahi kaha aapne")
        break
    else:
        print("Galat hai be!")
