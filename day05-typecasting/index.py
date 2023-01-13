a = "1"
# a = 1
b = "2"
# b = 2
print(int(a) + int(b))

# Python program to demonstrate
# implicit type Casting
 
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts
# b to float
b = 3.0
print(type(b))
 
# Python automatically converts
# c to float as it is a float addition
c = a + b
print(c)
print(type(c))
 
# Python automatically converts
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

# explicit typecasting
# int variable
a = 5
 
# typecast to str
n = str(a)
 
print(n)
print(type(n))