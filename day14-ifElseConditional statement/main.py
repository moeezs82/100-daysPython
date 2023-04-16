# Conditional operators
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# we use indentation instead of prantheses
while True:
    try:
        a = int(input("Enter your age: "))
        print("Your age is:", a)
        break
    except ValueError:
        print("Error: Please enter only integer values.")

if (a > 18):
    print("You can drive")
    print("Yes")
else:
    print("You cannot drive")
    print("No")
print("Yay!")

# Based on this, the conditional statements are further classified into following types:

# if
# if-else
# if-else-elif
# nested if-else-elif.
