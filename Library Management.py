class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}


    def displayBooks(self):

        print("We have following books in our library:",self.name)

        for book in self.bookslist:
            print(book)

    def lendbook(self, user, book):
        if book not in self.bookslist:
            print("please select books from the given available books only")
        elif book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender-Book database has been updated.You can take the book now ")

        else :
            print(f"Book is already being used by {self.lendDict[book]}")

    def addbook(self, book):
        self.bookslist.append(book)
        print("Book has been added to the book list")

    def returnbook(self, book):
            self.lendDict.pop(book)
if __name__=='__main__':
    shazia = Library(["Python", "Rich Daddy PoorDaddy", "Harry Potter", "C ++Basics", "Algorithms by CLRS"], "CodeWithShazia")
    while (True):
        print(f"Welcome to the {shazia.name} library.Enter your choice to continue")
        print("1.Display Books")
        print("2.Lend a Book")
        print("3.Add a book")
        print("4.Return a Book")
        user_choice = input()
        if user_choice not in ["1", "2", "3", "4"]:
            print("please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            shazia.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name :")
            shazia.lendbook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            shazia.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            shazia.returnbook(book)
        else:
            print("Not a valid option")
        print("press q to quit and c to continue")
        user_choice2 = " "
        while (user_choice2 !="c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 ==  "c":
                continue
