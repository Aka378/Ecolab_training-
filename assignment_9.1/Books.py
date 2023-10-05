class Book:
    def __init__(self, id, title, author, price, rating):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def find_by_author(self, author_name):
        books_by_author = []
        for book in self.books:
            if book.author == author_name:
                books_by_author.append(book)
        return books_by_author

    def find_by_rating_range(self, min_rating, max_rating):
        books_in_range = []
        for book in self.books:
            if min_rating <= book.rating <= max_rating:
                books_in_range.append(book)
        return books_in_range

    def find_by_price_range(self, min_price, max_price):
        books_in_range = []
        for book in self.books:
            if min_price <= book.price <= max_price:
                books_in_range.append(book)
        return books_in_range


# create some books
book1 = Book(1, "book1", "author1", 2000, 4.5)
book2 = Book(2, "book2", "author2", 1500, 4.2)


# create a bookstore to add books
bookstore = Bookstore()
bookstore.add_book(book1)
bookstore.add_book(book2)
bookstore.add_book(book3)
while True:
    print("\nMenu:")
    print("1. Find book by ID")
    print("2. Find books by author")
    print("3. Find books by rating range")
    print("4. Find books by price range")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = int(input("Enter book ID: "))
        found_book = bookstore.find_by_id(book_id)
        if found_book:
            print(f"Title: {found_book.title}, Author: {found_book.author}")
        else:
            print("Book not found.")
    elif choice == "2":
        author_name = input("Enter author's name: ")
        books_by_author = bookstore.find_by_author(author_name)
        print("\nBooks found by author:")
        for book in books_by_author:
            print(f"Title: {book.title}, Author: {book.author}")
    elif choice == "3":
        min_rating = float(input("Enter minimum rating: "))
        max_rating = float(input("Enter maximum rating: "))
        books_by_rating = bookstore.find_by_rating_range(min_rating, max_rating)
        print("\nBooks found by rating range:")
        for book in books_by_rating:
            print(f"Title: {book.title}, Rating: {book.rating}")
    elif choice == "4":
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        books_by_price = bookstore.find_by_price_range(min_price, max_price)
        print("\nBooks found by price range:")
        for book in books_by_price:
            print(f"Title: {book.title}, Price: ${book.price}")
    elif choice == "5":
        print("Exiting the search menu")
        break
    else:
        print("Invalid choice.")

