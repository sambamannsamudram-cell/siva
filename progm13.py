# Program 13: At Least One Even Number
# Even Number: If the number is divisible by 2 (Without any reminder)
# Logical or --> If any one of the combining condition is True, then the result is True.
# Arithmetic Operators
# / --> Division - result is in form of decimal value
# Example: 13/2 = 6.5
# // --> Floor Division - result is in form of integer
# Example: 13//2 = 6
# % --> Modulo - result is the reminder of the division operation
# Example: 13%2 = 1
# Reading the input from the user
n1 = int(input())
n2 = int(input())
print(n1%2==0 or n2%2==0)