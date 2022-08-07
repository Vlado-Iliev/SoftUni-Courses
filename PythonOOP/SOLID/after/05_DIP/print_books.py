class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:

    @staticmethod
    def format(book: Book) -> str:
        return book.content


class Printer(Formatter):

    def get_book(self, book: Book):
        return self.format(book)
