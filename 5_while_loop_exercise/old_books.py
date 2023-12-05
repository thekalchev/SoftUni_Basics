checked_books_count = 0
target_book = input()

while True:
    current_command = input()
    if current_command == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {checked_books_count} books.')
        break
    checked_books_count += 1

    if current_command == target_book:
        checked_books_count -= 1
        print(f'You checked {checked_books_count} books and found it.')
        break