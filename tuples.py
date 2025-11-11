#tuples introduction
#tuples are immutable (cannot be changed)
t1 = ("python", 4, 26, [1, 2, 3], True, (5, 6, 7))
print(type(t1))
print(len(t1))
print(t1[0])
print(t1[-1])
print(t1[3])
print(t1[5]) 

#tuples sequencing
t2 = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(len(t2))
print(type(t2))
print(t2[2:7])
print(t2[1:8:2])

#tuples operations
student_detail1 = (101 , "RIYA")
student_detail2 = (97, 45, 86, 79, 88)
print(type(student_detail1))
print(type(student_detail2))
student_details = student_detail1 + student_detail2
print(len(student_details))
print(student_details)
print(student_details.count(88))
print (student_details.index("RIYA"))

#tuples count method
fruits = ("apple", "banana", "cherry", "apple", "kiwi", "banana", "apple")
x = fruits.count("apple")
print(x)

t3 = (1, 0, 12, 95, 15, 2, 3, 4, 5, 1, 2, 1, 1, 1)
print(t3.count(1))

#tuples index method
fruits = ("apple", "banana", "cherry", "apple", "kiwi", "banana", "apple")
print(fruits.index("apple")) #first occurrence
print(fruits.index("banana", 2)) #searching from index 2
print(fruits.index("cherry", 0, 4)) #searching from index 0 to 4

#min,max and sum functions
print(min(t3))
print(max(t3))
print(sum(t3))  