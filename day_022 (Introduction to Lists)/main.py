
marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23, ['avinash', 'singh']]
print(marks)
print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

if "6" not in marks:
  print("Yes")
else:
  print("No")

# Same thing applies for strings as well!
if "Ha" in "Harry":
  print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1::2])

# lst = [i*i for i in range(int(input("Enter the number: ")))]
# print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)


# a = input(f'hii {lst} : ')
# print(a)


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) <= 4)]
print(namesWith_O)


