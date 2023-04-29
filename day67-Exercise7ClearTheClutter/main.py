# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png

import os

def renameTheFile(fileDir, fileExt):
    '''take a directory and file extension and rename related file to 1,2,3... order'''
    count = 0
    if fileExt[0] != '.':
        fileExt = '.' + fileExt
    if os.path.isdir(fileDir):
        for fileName in os.listdir(fileDir):
            if fileName.endswith(fileExt):
                count+=1
                newFileName = f"{count}{fileExt}"
                oldFilePath = os.path.join(fileDir, fileName)
                newFilePath = os.path.join(fileDir, newFileName)
                os.rename(oldFilePath, newFilePath)
        print("Operation Successful\n")
    else:
        print("Directory does not exist\n")

print("***Welcome to Clear The Clutter!***")
print("The Program will ask you to provide the complete directory path ex: F:/Learning/python/100daysPython and axtension for file you want to clear the clutter\n")
valid_inputs = ('y', 'e')
while True:
    user_input = input("If You want to change name enter y, enter e to exit the program: ").lower() 

    if user_input in valid_inputs:
        if user_input == 'y':
            fileDir = input("Please input Directory Name: ")
            fileExt = input("Please input File Extension: ")
            renameTheFile(fileDir, fileExt)
        else:
            break
    else:
        print("Invalid Input")