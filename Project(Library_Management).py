# using oop to create library
class library:
    def __init__(self, list, name):          # This are constructor for argument
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookList:
            print(book)


    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print(" Lender-Book has been updated. You can take the book now ")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print(" Book has been added to the book list ")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    My = library(['Python', 'Let us C', 'C++', 'Marvel', 'God of War'], "MyLibrary")

    while(True):
        print(f" Welcome to the {My.name} library. Enter your choice to continue ")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = int(input())

        if user_choice==1:
            My.displayBooks()
        elif user_choice==2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            My.lendBook(user, book)

        elif user_choice==3:
            book = input("Enter the name of book you want to add:")
            My.addBook(book)
        elif user_choice == 4:
            book = input("Enter the name of book you want to return:")
            My.returnBook(book)

        else:
            print("not a valid option")

        print("Press q to quit and c to continue")
        user_choice1 = ""
        while (user_choice1!="c" and user_choice1!="q"):
            user_choice1 = input()
            if user_choice1 =="q":
                exit()
            if user_choice1 =="c":
                continue



