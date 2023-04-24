def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello, world!")

hello()
# greet(hello)()

@greet
def printArgs(a: str, b: str):
    print("this is first var "+a+" this is second var "+b)

printArgs("hello", "world")

def addGreet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        result = fx(*args, **kwargs)
        print("Thanks for using this function")
        return result
    return mfx

@addGreet
def add(a: int, b: int):
    return a + b

sum = add(3, 2)
print(sum,'\n\n\n')

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b
print(my_function(1,4))
