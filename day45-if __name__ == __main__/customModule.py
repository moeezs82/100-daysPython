def customFunction():
    print("custom function that is already calling in this file")


# in order to make this function call only when this file executes
print(__name__)  # will print __main__ if executed directly and print file name(in this case customMethod) if run from outside
if __name__ == '__main__':
    customFunction()