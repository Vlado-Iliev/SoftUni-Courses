wanted_book = input()
book_counter = 0
current_book = input()
book_found = False

while current_book != 'No More Books':
    if current_book == wanted_book:
        book_found = True
        break
    book_counter += 1
    current_book = input()

if book_found:
    print(f'You checked {book_counter} books and found it.')
else:
    print('The book you search is not here!')
