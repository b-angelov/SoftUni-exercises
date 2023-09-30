class Book:
    def __init__(self,*args):
        self.name,self.author,self.pages = args


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
