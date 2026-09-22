
result=(10+5)*2
print(result)


#use while when repetition depends on condition
for i in range(1,6):
    print(i)

    
i=1
while i <= 5:
    print(i)
    i= i+1


for i in range(1,11):
    print(i)

    for i in range(10,0,-1):
        print(i)

#even numbers
for  i in range(2, 51, 2):
    print(i)

#odd numbers
for i in range(1,51,2):
    print(i)

#print multiples
for i in range(5,51,5):
    print(i)

#tables of loops
number = int(input("enter number:"))
for i in range(1,11):
    print(number, "x", i, "=", number * i)

#sum of numbers from 
n = int(input("enter n:"))
total = 0
for i in range(1,n +1):
    total=total + i
print("sum:",total)

#factorial of a number
n = int(input("enter number:"))
factorial =1
for i in range(1,n+1):
    factorial = factorial * i
print("factorial:", factorial)


#sum of even numbers from 2 to n
n = int(input("enter n:"))
total = 0
for i in range(2,n+1,2):
    total = total + i

print("sum:",total)
#count of multiples of 3
n = int(input("enter n:"))
count = 0
for i in range(1,n+1):
    if i % 3 ==0:
        count = count+1
print("count:",count)


#sum of multiples of 5
n = int(input("enter n:"))
total = 0
for i in range(1,n+1):
    if i % 5 == 0:
        total = total + i
print("sum: ",total)



i=2
while i<= 50:
    print(i)
    i = i+2







#print total of numbers entered by user until 0 is entered
total = 0
number = int(input("enter number"))
while number !=0:
    total = total + number
    number = int(input("enter number:"))
    print("total:",total)

