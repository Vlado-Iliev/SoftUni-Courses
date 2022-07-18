from project.user import User


class Library:
    def __init__(self):
        self.user_records = list()
        self.books_available = dict()
        self.rented_books = dict()

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        for writer, collection in self.books_available.items():
            if writer == author:
                for book in collection:
                    if book == book_name:
                        user.books.append(book_name)
                        self.books_available[author].remove(book_name)
                        self.rented_books[user.username] = {book_name: days_to_return}
                        return f"{book_name} successfully rented for the next {days_to_return} days!"
        for username, rented_book in self.rented_books.items():
            for key,value in rented_book.items():
                if key == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {value} days!'

    def return_book(self,author:str, book_name:str, user: User):
        for book in user.books:
            if book == book_name:
                user.books.remove(book_name)
                for key in self.rented_books[user.username]:
                    if key == book_name:
                        self.rented_books[user.username].pop(key)
                        return
                self.books_available[author].append(book_name)
        return f"{user.username} doesn't have this book in his/her records!"



