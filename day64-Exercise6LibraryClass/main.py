# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

import sys

class CustomLibrary:
    def __init__(self, books: list):
        self.books = books
        self.no_of_books = len(books)
    def addBooks(self, books: list):
        self.books+=books
        self.no_of_books+=len(books)
        print("Books added successfully")
    def emptyLibrary(self):
        self.books.clear()
        self.no_of_books = 0
    def showInfo(self):
        print(f"Total no. of books: {self.no_of_books}")
        print(f"List of books: {self.books}")
    def compare(self):
        print(f"len of books list: {len(self.books)}")
        print(f"No. of books variable: {self.no_of_books}")
        if len(self.books) == self.no_of_books:
            print("All OK comparison correctly")
        else:
            print("Something wrong shutting down the program")
            sys.exit()

print('***Welcome to Library management system***\n')

input("Enter any key to create a new library\n")

userLibrary = CustomLibrary([])

valid_input = ('n', 'i', 'c', 'e', 'exit')
while True:
    userInput = input("Enter N to add new books in library, I to show all books and number of books, C to compare the variables and E to Empty the library. to exit program type \"exit\": ").lower()

    if userInput not in valid_input:
        print("**Invalid Input**")
    else:
        if userInput == "exit":
            print("Thank you for using this program.")
            break
        elif userInput == "e":
            userLibrary.emptyLibrary()
            userLibrary.showInfo()
        elif userInput == "c":
            userLibrary.compare()
        elif userInput == "i":
            userLibrary.showInfo()
        else:
            newBooks = input("Please enter comma separated names of books: ")

            # Split the user input by comma, and strip the spaces from each item in the resulting list
            bookList = [book.strip() for book in newBooks.split(',')]
            
            userLibrary.addBooks(bookList)

