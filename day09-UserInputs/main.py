# name = input("Enter your name: ")
# print("Your input name is:", name)

# num_1 = input("Enter First Number: ")
# num_2 = input("Enter Second Number: ")

# print(num_1+num_2)


# advance topic to handle error
while True:
    try:
        num_1 = int(input("Enter First Number: "))
        num_2 = int(input("Enter Second Number: "))
        break
    except ValueError:
        print("Error: Please enter only integer values.")

print("addition of your input is:", num_1+num_2)
