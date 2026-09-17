# Program 16: Exchange Values of Two Variables
# Reading the input from the user
a = int(input())
b = int(input())

# Logic 1 - Using temp variable
temp = a
a = b
b = temp
print(a)
print(b)

# Logic 2: Without using temp (3rd variable)
a=a+b
b=a-b
a=a-b
print(a)
print(b)

# Logic 3: Without using temp (3rd variable)
a = a^b
b = a^b
a = a^b
print(a)
print(b)

# Logic 4: Without using temp (3rd variable)
# Problem: It cannot handle 0
a = a*b
b = a/b
a = a/b
print(a)
print(b)

# Logic 5: Using Python's Special
# Simplest Way
a,b = b,a
print(a)
print(b)