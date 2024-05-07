
tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
print(res)
res = tuple1.index(3)
print(res)
# res = tuple1.index(311)   # will throw an error
# print(res)
res = tuple1.index(3, 4, 8)
print(res)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)


countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
print(temp)
countries = tuple(temp)
print(countries)


countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)


# tuple.count(element)

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
res2 = Tuple1.count(1)  # it only takes one argument
print('Count of 3 in Tuple1 is:', res)
print(res2)
print(Tuple1.count(2))


# tuple.index(element, start, end)

Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)
print(Tuple1.index(2))
res = Tuple.index(3,4,8)    # 3 is value & 4,8 is range of index
print(res)

