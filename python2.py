a=10
b=3
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("Remainder:", a%b)
print("power:", a**b)



#simple calculator
a=int(input("Enter first number"))
b=int(input("Enter second number"))

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)


#student marks calculator
name=input("Enter student name:")

m1=int(input("enter python marks:"))
m2=int(input("enter java marks:"))
m3=int(input("enter sql marks:"))

total=m1+m2+m3
average=total/3

print("\n------Student Marks Report---")
print("name:", name)
print("Total marks:", total)
print("Average marks:", average)

#shopping bill calculator
price1=int(input("enter product 1 price:"))
price2=int(input("enter product 2 price:"))
price3=int(input("enter product 3 price:"))

total=price1+price2+price3

discount=total*0.10
finalamount=total-discount