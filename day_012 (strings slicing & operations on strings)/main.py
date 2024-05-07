
fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:8]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])  # it will start from 0th index
print(fruit[1:])  # it will iterate till end
print(fruit[:])   # it will iterate from 0th index to last index
print(fruit[0:-3])  # -3 means len(fruit)-3 = 2 [0:2]
print(fruit[:len(fruit)-3])
print(fruit[len(fruit)-4:])
print(fruit[-4:])   # len(fruit)-4 = 1
print(fruit[-1:len(fruit) - 3]) # 4:2
print(fruit[-3:-1])   # len(fruit)-3 : len(fruit)-1 = 2:4

# Quick Quiz:
nm = "Avinash"
print(nm[-4:-2])  # output = na
# @avinashsanjaysingh
