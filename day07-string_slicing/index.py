fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5])

# both same
print(fruit[0:-3])
print(fruit[:len(fruit)-3])

# both same
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])