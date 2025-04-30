from models import (Book, Base,
                    session, engine)


# main menu with search, add, view, ananlysis and exit
def main_menu():
    print("Welcome to the Book Store")
    print("1. Search for a book")
    print("2. Add a new book")
    print("3. View all books")
    print("4. Analysis")
    print("5. Exit")

# func to search for a book
def search_book():
    print("Search for book by:")
    print("1. Title")
    print("2. Author")
    print("3. Date Published")
    print("4. Price")
    choice = input("Enter your choice: ")

# function to search for a book by title    
def search_by_title():
    print("Search queries are case sensitive.")
    title = input("Enter the title of the book: ")
    book = session.query(Book).filter_by(title=title).first()
    if book:
            print(f"Book found: {book}")
    else:
        print("Book not found.")
        print("Please check your spelling.")

# function to search for a book by author
def search_by_author():
    print("Search queries are case sensitive.")
    author = input("Enter author's name: ")
    book = session.query(Book).filter_by(author=author).all()
    for book in book:
        print(f'{book.title} by {book.author} published on {book.date_published} for {book.price}')
# function to add a new book
# func to edit book
# func to delete book
# while loop to keep the program running

if __name__ == '__main__':
    pass