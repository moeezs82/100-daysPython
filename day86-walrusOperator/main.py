# walrus operator allows user to assign a value to a variable in an expression

# print(a:=True)

# numbers = [1, 2, 3, 4, 5]

# while(n:=len(numbers)):
#     print(numbers.pop())
#     print(f"Value of n is: {n}")

foods = list()

# without walrus
# while True:
#     food = input("What food would you like: ")
#     if food != "quit":
#         break
#     foods.append(food)



while(food:=input("What food would you like: ")) != "quit":
    foods.append(food)
