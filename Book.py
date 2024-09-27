class Book:
    def __init__(self , bookID  = "" , bookName = "" , bookAuthor  = "" , bookPageNumber  = 200, bookPublishing  = "" , bookYear = 2004):
        self.bookID = str(bookID)
        self.bookName = str(bookName)
        self.bookAuthor = str(bookAuthor)
        self.bookPageNumber = int(bookPageNumber)
        self.bookPublishing = str(bookPublishing)
        self.bookYear = int(bookYear)

    def getBookID(self) -> str:
        return self.bookID

    def setBookID(self, bookID):
        self.bookID = bookID

    def getBookName(self) -> str:
        return self.bookName

    def setBookName(self, value):
        self.bookName = value
        
    def getBookAuthor(self) -> str:
        return self.bookAuthor

    def setBookAuthor(self, bookAuthor):
        self.bookAuthor = bookAuthor

    def getBookPageNumber(self) -> int:
        return self.bookPageNumber

    def setBookPageNumber(self, bookPageNumber):
        self.bookPageNumber = bookPageNumber

    def getBookPublishing(self) -> str:
        return self.bookPublishing

    def setBookPublishing(self, bookPublishing):
        self.bookPublishing = bookPublishing

    def getBookYear(self) -> int:
        return self.bookYear

    def setBookYear(self, bookYear):
        self.bookYear = bookYear

    def input(self):
        self.bookID = input("enter bookID: ")
        self.bookName = input("enter bookName: ")
        self.bookAuthor = input("enter bookAuthor: ")
        self.bookPageNumber = int(input("enter bookPageNumber: "))
        self.bookPublishing = input("enter bookPublishing: ")
        self.bookYear = int(input("enter bookYear: "))
        
    def __str__(self) -> str:
        return f"{self.bookID}~{self.bookName}~{self.bookAuthor}~{self.bookPageNumber}~{self.bookPublishing}~{self.bookYear}\n"
        
         