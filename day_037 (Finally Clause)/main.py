
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)


# Syntax:
'''
try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation
'''


try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")

'''
# output1:
Enter an integer: 19
Integer Accepted.
This block is always executed.

# output2:
Enter an integer: 19
Integer Accepted.
This block is always executed.
'''