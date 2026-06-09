#1Question
name = "Sanskriti"
print("First character:", name[0])
print("Last character:", name[-1])
print("Length:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Reverse:", name[::-1])

#2Question
s = "PythonProgramming"
print("First four characters:", s[:4])
print("Characters from index 2 to 5:", s[2:6])
print("Reverse string:", s[::-1])

#3Question
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

numbers.insert(2, 2.5)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.pop()
print(numbers)

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

print("Length of list:", len(numbers))

print("Count of 2.5:", numbers.count(2.5))

#4Question
subjects = ("English", "SST", "Chemistry", "Math", "Computer")

print("First element:", subjects[0])
print("Last element:", subjects[-1])
print("Length:", len(subjects))
print("Slicing:", subjects[1:4])

nums = (89, 49, 99, 85, 35)

print("Maximum:", max(nums))
print("Minimum:", min(nums))
print("Sum:", sum(nums))

#5Question
student = ("Sanskriti", 20, "CSAI", "Jaipur")

name, age, course, city = student

print("Name:",name)
print("Age:",age)
print("Course:",course)
print("City:",city)

#6Question
student = {
    "Name": "Sanskriti",
    "Age": 20,
    "Course": "B.Tech",
    "Address": "Jaipur"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student["Address"] = "Rajasthan"
print("Updated Address:", student)

student["Branch"] = "CSAI"
print("After Adding Branch:", student)

#7Question
lst = [1, 2, 3, 4, [2, 5], 7]

print(lst[4][1])


#8Question
num = int(input("Enter a number: "))

num += 10

print("Updated value:", num)

#9Question
a = input("Enter first number: ")
b = input("Enter second number: ")

a = int(a)
b = int(b)

print("Multiplication =",a * b)

#10Question
student = {
    "Name": "Sanskriti",
    "Age": 20,
    "Course": "B.Tech"
}

print("get():", student.get("Age"))
print("keys():", student.keys())
print("values():", student.values())
print("items():", student.items())

#11Question
list1 = [1, 2, 3, 4, 5]

list2 = list1.copy()

print("Original List:", list1)
print("Copied List:", list2)