"""
numbers=[10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)

#list in python
  #list is an ordered and changeable collection that can be store
marks =[80,90,75,85]
print(marks)

#index elements
numbers=[10,20,30,40,50,60,70,80,90]
print(numbers.index(30))


#sorting elements
numbers = [10,20,30,40,20,80,20]
print(numbers.count(20))

#acess values in atuple
student=("bhargavi", 21,85.5)
print(student[0])
print(student[1])
print(student[2])

#tuples are immutable, meaning they cannot be changed after they are created. However, if the tuple contains mutable objects, such as lists, those objects can be modified.
numbers = (10,20,20,30,20)
print(numbers.count(20))

numbers=(10,20,30,40)
print(numbers.index(30))

numbers=[10,20,30,40]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
numbers={10,20,30,20,10}
print(numbers)

#suppose students have selected subjects
subjects = {"python", "java", "python", "sql", "java"}
print(subjects)


#add values to a set
subjects = {"python", "java"}
subjects.add("sql")
print(subjects)

#remove values from a set
subjects.remove("java")

#sets do not allow duplicate values
numbers={1,2,3,4,}
"""

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(numbers[1::2])
print(numbers[::2])
print(numbers["even"])
print(numbers["odd"])
''''''