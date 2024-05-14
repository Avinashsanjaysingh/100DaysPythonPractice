
#  python 3.7 onwards dictionary is ordered, before it was unordered.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 
print(info.keys())
print(info.values())

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
  

print()

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())

