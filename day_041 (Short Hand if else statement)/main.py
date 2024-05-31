
a = 33000
b = 3303
print(a) if a > b else print("=") if a == b else print(b)

c = 9 if a>b else 0
print(c)

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# Syntax

'''
result = value_if_true if condition else value_if_false

# This syntax is equivalent to the following if-else statement:

if condition:
    result = value_if_true
else:
    result = value_if_false
'''