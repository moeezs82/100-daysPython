import os

def removeSymbol(directoryPath, extension, countRename = 0):
    '''this function will take a directory name and check for subdirectories and remove '-' file with given extension'''
    
    # checking if the directory exists
    if (os.path.isdir(directoryPath)):
        for fileName in os.listdir(directoryPath):
            folderName = f"{directoryPath}\{fileName}"
            if (os.path.isdir(folderName)):
                # if current path is directory then recursive calling the function
                # sending countRename as it is incraese when file deleted
                countRename=removeSymbol(folderName, extension, countRename)
            elif (fileName.endswith(extension)):
                # counting the deleted files
                countRename+=1
                newFileNameList = fileName.split('-')
                newFileName = ''
                for elem in newFileNameList:
                    if str(elem) == 'shirt':
                        newFileName += '-'+elem
                    else:
                        newFileName += ' '+elem
                oldFilePath = os.path.join(directoryPath, fileName)
                newFilePath = os.path.join(directoryPath, newFileName)
                os.rename(oldFilePath, newFilePath)

    else:
        print("Directory does not exist")
    
    return countRename


fileRename = removeSymbol('F:/Learning/python/fileToRename', '.webp')

print(f"{fileRename} files renamed")

