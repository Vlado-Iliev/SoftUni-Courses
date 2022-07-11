class Book:
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages


   # def __str__(self):
    #    return self

book = Book("My Book", "Me", 200)

print(book.name)

print(book.author)

print(book.pages)