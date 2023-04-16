while True:
    try:
        num = int(input("Enter some Integer: "))
        break
    except ValueError:
        print("You Enter invalid Integer")

if(num < 0):
    print("You entered negative Integer")
elif(num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("You entered 0")