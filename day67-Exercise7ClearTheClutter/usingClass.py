import os

class ClutterClearer:
    file_dir = os.getcwd()
    file_ext = '.txt'
    def __init__(self, file_dir, file_ext):
        self.file_dir = file_dir
        self.file_ext = file_ext

    @classmethod
    def set_dir_ext(cls, dir, ext):
        cls.file_dir = dir
        cls.file_ext = ext
    
    @classmethod
    def rename_files(cls):
        '''take a directory and file extension and rename related file to 1,2,3... order'''
        count = 0
        if cls.file_ext[0] != '.':
            cls.file_ext = '.' + cls.file_ext
        if os.path.isdir(cls.file_dir):
            for file_name in os.listdir(cls.file_dir):
                if file_name.endswith(cls.file_ext):
                    count += 1
                    new_file_name = f"{count}{cls.file_ext}"
                    old_file_path = os.path.join(cls.file_dir, file_name)
                    new_file_path = os.path.join(cls.file_dir, new_file_name)
                    os.rename(old_file_path, new_file_path)
            print("Operation Successful\n")
        else:
            print("Directory does not exist\n")
            
    def rename_files(cls):
        '''take a directory and file extension and rename related file to 1,2,3... order'''
        count = 0
        if cls.file_ext[0] != '.':
            cls.file_ext = '.' + cls.file_ext
        if os.path.isdir(cls.file_dir):
            for file_name in os.listdir(cls.file_dir):
                if file_name.endswith(cls.file_ext):
                    count += 1
                    new_file_name = f"{count}{cls.file_ext}"
                    old_file_path = os.path.join(cls.file_dir, file_name)
                    new_file_path = os.path.join(cls.file_dir, new_file_name)
                    os.rename(old_file_path, new_file_path)
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
            file_dir = input("Please input Directory Name: ")
            file_ext = input("Please input File Extension: ")

            # using class
            ClutterClearer.set_dir_ext(file_dir, file_ext)
            ClutterClearer.rename_files()
            
            # using instance
            # clutter_clearer = ClutterClearer(file_dir, file_ext)
            # clutter_clearer.rename_files()
        else:
            break
    else:
        print("Invalid Input")
