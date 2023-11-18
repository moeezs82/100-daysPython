import os

class ClutterClearer:
    file_dir = os.getcwd()

    def __init__(self, file_dir):
        self.file_dir = file_dir

    @classmethod
    def set_dir(cls, dir):
        cls.file_dir = dir
    
    @classmethod
    def rename_files(cls):
        '''take a directory and rename files name by replace ' ' to '-' order'''
        count = 0
        if os.path.isdir(cls.file_dir):
            for root, dirs, files in os.walk(cls.file_dir):
                # Rename files
                for file_name in files:
                    file_name_without_ext, file_ext = os.path.splitext(file_name)
                    modified_string_hyphens = file_name_without_ext.replace(' ', '-')
                    new_file_name = f"{modified_string_hyphens}{file_ext}"
                    old_file_path = os.path.join(root, file_name)
                    new_file_path = os.path.join(root, new_file_name)
                    os.rename(old_file_path, new_file_path)

                # Rename directories
                for dir_name in dirs:
                    modified_dir_name = dir_name.replace(' ', '-')
                    old_dir_path = os.path.join(root, dir_name)
                    new_dir_path = os.path.join(root, modified_dir_name)
                    os.rename(old_dir_path, new_dir_path)
            print("Operation Successful\n")
        else:
            print("Directory does not exist\n")

print("\n\n***Welcome to Clear The Clutter!***")
print("The Program will ask you to provide the complete directory path ex: F:/Learning/python/100daysPython for file you want to clear the clutter\n")
valid_inputs = ('y', 'e')
while True:
    user_input = input("If You want to change name enter y, enter e to exit the program: ").lower() 

    if user_input in valid_inputs:
        if user_input == 'y':
            file_dir = input("Please input Directory Name: ")

            # using class
            ClutterClearer.set_dir(file_dir)
            ClutterClearer.rename_files()
            
        else:
            break
    else:
        print("Invalid Input")
