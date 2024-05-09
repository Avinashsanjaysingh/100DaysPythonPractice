
# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1


def fact(num):
  match num:
    case 0: 
      return 1
    case 1: 
      return 1
    case _: 
      return (num * fact(num-1))

print(fact(5))

def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number:",num)
print("Factorial:",factorial(num))

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....

def fib(n):
  list = [0,1]
  a = 0
  b = 1
  i = 0
  
  if n == 0:
    list = []
  elif n == 1:
    list = [0]
  elif n >= 2:
    while (i < n-2):
      b += a
      a = b-a
      list.append(b)
      i +=1
  print(list)

print(fib(10))


# def seq(n):
#   num1 = 0
#   num2 = 1
#   next_number = num2 
#   count = 1

#   if n == 1:
#     print('0', end='')
#   else:
#     print('0 1 ', end='')
#   while count <= n-2:
#     print(next_number, end=" ")
#     count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2
#   print()

# print(seq(6))
