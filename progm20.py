# Program 20:  Sum of Digits of a Two-Digit Number
num = int(input())  # num = 48
tens = num//10      # tens =  48//10 = 4
units = num%10      # units = 48%10 = 8
total = tens + units # total = 4+8 = 12
print(total)