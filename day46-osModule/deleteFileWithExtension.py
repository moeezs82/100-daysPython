import os

# Get the directory of the current script file
dir_path = os.path.dirname(os.path.realpath(__file__))

def DltFileWithExtension(directoryPath, extension, countDeleted = 0):
    '''this function will take a directory name and check for subdirectories and delete file with given extension'''
    
    # checking if the directory exists
    if (os.path.isdir(directoryPath)):
        for fileName in os.listdir(directoryPath):
            folderName = f"{directoryPath}\{fileName}"
            if (os.path.isdir(folderName)):
                # if current path is directory then recursive calling the function
                # sending countDeleted as it is incraese when file deleted
                countDeleted=DltFileWithExtension(folderName, extension, countDeleted)
            elif (fileName.endswith(extension)):
                # counting the deleted files
                countDeleted+=1
                os.remove(os.path.join(directoryPath, fileName))

    else:
        print("Directory does not exist")
    return countDeleted


print("\033[41m\nWarning please place the program file just outside the directory from which you want remove file with given extension\033[0m \n")

while True:
    confirmed = input("Did you place the file to the right place? y to confirm n to terminate: ")
    if (confirmed.lower() == 'y'):
        folder_name = input("Please input the folder name (folder\sub)or(mainfolder): ")
        folder = os.path.join(dir_path, folder_name)
        extension_to_remove = input("Please input the extension to remove: ")
        while True:
            confirm_again = input(f"\n\033[41mAre you sure you want to remove all file with {extension_to_remove} extension from {folder} directory and subdirectories: [y or n]:\033[0m ")
            if(confirm_again.lower() == 'y'):
                deletedFiles = DltFileWithExtension(folder, extension_to_remove)
                if(deletedFiles != 0):
                    print("Task completed successfully")
                print(f"Total Deleted Files: {deletedFiles}")
                break
            elif (confirm_again.lower() == 'n'):
                print("program terminated")
                break
            else:
                print("\nInvalid input")

        break
    elif (confirmed.lower() == 'n'):
        print("Please change the directory place...")
        break
    else:
        print("\nInvalid input")


        