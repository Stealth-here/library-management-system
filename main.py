from dp import init_db
from functions import add_book, view_book, search_book, update_book, delete_book

def main():
    while True:
        print('\n Library Management System')
        print('1. Add Book')
        print('2. View Books')
        print('3. Update Book')
        print('4. Delete Book')
        print('5. Exit')

        choice = input('Enter your choice:')
        try:
            if choice=='1':
                title = input('Enter book title:')
                author = input('Enter book author:')
                year = int(input('Enter publication year:'))
                isbn = input('Enter ISBN number:')
                add_book(title, author, year, isbn)
                print("Book added successfully!")
            if choice=='2':
                books = view_book()
                for book in books:
                    print(book)
            if choice=='3':
                book_id = int(input('Enter book ID to update:'))
                title = input('Enter new book title:')
                author = input('Enter new book author:')
                year = int(input('Enter new publication year:'))
                isbn = input('Enter new ISBN number:')
                update_book(book_id, title, author, year, isbn)
                print("Book updated successfully!")
            if choice=='4':
                book_id = int(input('Enter book ID to delete:'))
                delete_book(book_id)
                print("Book deleted successfully!")
            if choice=='5':
                print("Exiting the program.")
                break
        except:
            print("Please enter a valid input")
    
if __name__ == '__main__':
    main()
