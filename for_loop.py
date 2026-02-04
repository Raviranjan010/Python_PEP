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


