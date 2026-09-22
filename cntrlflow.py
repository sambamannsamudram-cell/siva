"""

marks =int(input("enter marks"))

if marks >= 40:
    print("pass")
else:
    print("fail")
    ...
number = int(input("enter a number"))
if number >= 0:
    print("positive")
else:
    print("negative")
    ...
    #control statements
age = int(input("enter your age"))
if age >= 18:
    print("eligible")
else :
    print("not eligible")
    ...

    marks = int(input("enter your marks"))
    if marks >=45:
        print("pass")
    else :
        print("fail")
...
number = int(input("enter a number:"))
if number > 100:
    print("number is greater than 100")
else:
    print("number is not greater than 100")
    ...


marks = (int(input("enter your marks: ")))
if marks >= 90:
    print("grade a")
elif marks >= 75:
    print("grade b")
elif marks >= 60:
    print("grade c")
elif marks >= 40:
    print("grade d")
else:
    print("fail")



a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if a>b:
    print("largest:",a)
elif b > a:
    print("largest:",b)
elif c>b:
    print("largest:",c)
else :
    print("all are equal")
    
number = int(input("enter a number:"))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")


a = float(input("enter first number"))
b = float(input("enter second number"))
operator = input("enter operator(+,-,*,/):")
if operator == "+":
    print("result:", a+b)
elif operator == "-":
    print("result:", a-b)
elif operator == "*":
    print("result:", a*b)
elif operator == "/":
    if b != 0:
        print("result:", a/b)
    else:
        print("cannot divide by zero")
else:
    print("invalid operator")
    

username = input("enter username")
password = input("enter password")
if username == "admin" :
    if password == "1234":
        print("login successful")
    else:
        print("wrong password")
else:
    print("wrong username")
    

marks = int(input("enter marks:"))
attendance = float(input("enter attendance percentage:"))
if marks >= 40:
    if attendance >=75:
        print("eligible")
    else:
        print("not eligible due to attendance")
else:
    print("fail")


balance = float(input("enter balance"))
amount = float(input("enter withdrawal amount"))
if amount > 0:
    if amount <= balance:
        balance = balance - amount
        print("withdrawal sucessful")
        print("remainig balance:", balance)
    else:
        print("insufficient balance")
else:
    print("invalid amount")
    

age = int(input("enter age"))
test = input("did you pass the driving test? (yes/no):")
if age >=18:
    if test == "yes":
        print("license can be issued")
    else:
        print("pass the driving test first")
else:
    print("not eligible due to age")    


result = (10+5) *2
print(result)

"""



