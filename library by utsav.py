# create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)
# dictionary (books - nameofperson)
# create a main function and run an infinite while loop asking users for their input

class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def display(self):
        print(f"We have following books in our Library: {self.name}")
        for books in self.booksList:
            print(books)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book : user})
            print("Lender-Books database has been updated, You can take the book now")
        else:
            print(f"The book is already being used by {self.lendDict[book]}")


    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the Book List")


    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    harry = Library(['python', 'Rich dad poor dad', 'harry potter', 'c++ basics', 'CLRS'], "CodewithUtsav")

    while(True):
        print(f"Welcome to the {harry.name} library. Enter your choice to continue")
        print("1. Display")
        print("2  Lend a book")
        print("3  Add a book")
        print("4 Return a book")

        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
        else:
            user_choice = int(user_choice)


        if user_choice ==1:
            harry.display()

        elif user_choice == 2:
            book  = input("Enter the name of the book you want to lend:")
            user = input("Enter your name:")
            harry.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            harry.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            harry.returnBook(book)
        else:
            print("not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2 == 'c' and user_choice2!='q'):
            user_choice2 = input()
            if user_choice2 == 'q':
                exit()

            elif user_choice2 == 'c':
                continue
