
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {123: 60, 222: 67, 566: 90}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
# ep1.popitem()
# del ep1[122]
# del ep1
print(ep1) 

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
# print(info)   # NameError: name 'info' is not defined