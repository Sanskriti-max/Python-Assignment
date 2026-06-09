#_2 = 10
#print(_2)
#data type = 0(int,float,bool,str,list,tuple,set,dict)
#name = "sanskriti"
#print("this is my name",name)
#print("type of my string is",tuple(name))
#print("len of my string is",len(name))

#print("indexing........")
#print(name[0])
#print(name[6])
#slicing
#print(name[0:5])
#print(name[0:9:2])
#print(name[0:10])
#print(name[::-1])
#print(name.upper())
#print(name.title())
#print(name.index("s"))
#print(name.count("i"))
#print(name.index("t"))
#print(name.replace("s","k"))
#print(name.upper())
#print(name.index("i"))
#str = "Hello"
#print(str)
#str = 10
#print(str)
#list = 19
#print(list)
#num="1234"
#print(num)
#print(type(num))
#print(num.isdigit())
#print(num.isalpha())
#print(num.isalnum())
#char="sanskriti modwel"
#print(char.split())
#print(char.strip())
#name = "sanskriti"
#address = "prem nagar"
#print(f"My name is {name} and I live in {address}")
      
#path = r"C:\Users\hp\OneDrive\Desktop\training\python>"
#print(path)
#import os
#print(os.listdir(path))

#college = "anand"
#print("an" in college),
#list = (mutable,dublicate,ordered,Hetrogenues)
#lst = [1,2,3,4,5,6,"khushi"]
#print(list)
#print(list[3])
#print(list[0:5])
#print(list.append("sanskriti"))
#lst.append("sanskriti")
#print(lst)
#list=(1,2,3,)
#lst.extend([4,"khushi"])
#print(list)

#lst = [1,2,3,[8,9],4,5,6,"khushi"]
#print(lst)
#print(lst.remove("khushi"))
#lst.reverse()
#print(lst)
#print(lst[3][0])
#lst = [1,2,3,4,5]
#lst2 = [3]

#tuple(immutable,oredred,hetro,duplicate)

#tpl = (1,2,3,4,5,6,"khushi")
#print(tpl)
#print("This is my tuple",tpl)
#print("len of my tuple",len(tpl))
#print("Type of my tuple",type(tpl))
#print(tpl[3])
#print(tpl[2:4])
#print("tuple unpacking")
#a, b, c = (1,2,3)
#print(a)
#print(b)
#print(c)

#a = 1,2,3,4,5,6
#print(a)
#print(type(a))
#print(len(a))

#typecasting

#tpl = (1,2,3,4,5,7,"khushi")
#print(len(tpl))
#print(type(tpl))

#lst = list(tpl)
#print(lst)
#print(tuple(lst))
#print(len(lst))
#lst.append(4)
#print(lst)
#lst.extend([9,10])
#print(lst)
#print(3 in lst)

#student = {"name":"sanskriti","roll no":28,"Age":21,"Branch":"CS(AI)"}
#print("This is my dict",student)
#print(len(student))
#print(type(student))
#print(student["name"])
#print(student["Branch"])
#print(student.get("name"))
#print(student.keys()) 
#print(student.values())  
#print(student.items())
#student["CGPA"] = 9.9
#print(student)
#student["name"] = "yash"
#print(student)
#student["name"] = "sanskriti","yash"
#print(student)
#{deep copy
#copy,how to change the value of dict..pop,set default.
#update}medium
#print(student)
#user = input("Enter the key")
#print(student)

#<<<<<<<<<<<<<<<<<<<set>>>>>>>>>>>>>>>>>>
#sat = {1,2,3,4,5,6,"khushi"}
#print("this is my sat",sat)
#print("type of my sat",type(sat))
#print("len of my sat",len(sat))
#sat.add(10)
#print(sat)
#sat.remove(6)
#print(sat)
#sat.discard(2)
#print(sat)

#lst = [1,1,2,3,3,2,4,6,5,5,6,4,7,7,7,7]
#sat = sat(list)
#print(sat)

#lst = [1,1,2,3,3,2,4,6,5,5,6,4,7,7,7,7]
#s = set(lst)
#print(s)

#sat1 = {1,2,3,4}
#sat2 = {3,4,5,6}
#print(sat1.union(sat2))
#print(sat1)
#print(sat1.intersection(sat2))

#Operators---------------------------------------------------------------------------------
# ==========================
# 1. Arithmetic Operators
# ==========================

a = 10
b = 3

print("Addition:", a + b)          # +
print("Subtraction:", a - b)       # -
print("Multiplication:", a * b)    # *
print("Division:", a / b)          # /
print("Floor Division:", a // b)   # //
print("Modulus:", a % b)           # %
print("Power:", a ** b)            # **


# ==========================
# 2. Comparison Operators
# ==========================

print(a == b)   # Equal to
print(a != b)   # Not equal to
print(a > b)    # Greater than
print(a < b)    # Less than
print(a >= b)   # Greater than or equal to
print(a <= b)   # Less than or equal to


# ==========================
# 3. Assignment Operators
# ==========================

x = 5
print(x)

x += 2
print(x)

x -= 2
print(x)

x *= 3
print(x)

x /= 3
print(x)

x //= 2
print(x)

x %= 2
print(x)

x = 2
x **= 3
print(x)


# ==========================
# 4. Logical Operators
# ==========================

p = True
q = False

print(p and q)
print(p or q)
print(not p)


# ==========================
# 5. Membership Operators
# ==========================

lst = [1, 2, 3, 4, 5]

print(3 in lst)
print(10 in lst)
print(10 not in lst)


# ==========================
# 6. Identity Operators
# ==========================

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)


# ==========================
# 7. Bitwise Operators
# ==========================

a = 5      # 0101
b = 3      # 0011

print(a & b)   # AND
print(a | b)   # OR
print(a ^ b)   # XOR
print(~a)      # NOT
print(a << 1)  # Left Shift
print(a >> 1)  # Right Shift
















