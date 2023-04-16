# 7! = 7*6!
# 6! = 6*5! and so on
# here comes the concept of recurcive functions

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(3))
print(factorial(4))
print(factorial(5))