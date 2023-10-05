class Book:
    def __init__(self, id, title, author, price, rating):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating
        self.previous = None  # Previous book in the linked list
        self.next = None  # Next book in the linked list

class Bookstore:
    def __init__(self):
        self.head = None  # Initialize the linked list with an empty head node

    def add_book(self, book):
        new_book = Book(book.id, book.title, book.author, book.price, book.rating)
        if not self.head:
            self.head = new_book
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_book
            new_book.previous = curr  # Set the previous book for the new book

    def find_by_id(self, book_id):
        curr = self.head
        while curr:
            if curr.id == book_id:
                return curr
            curr = curr.next
        return None

    def find_by_author(self, author_name):
        books_by_author = []
        curr = self.head
        while curr:
            if curr.author == author_name:
                books_by_author.append(curr)
            curr = curr.next
        return books_by_author

    def find_by_rating_range(self, min_rating, max_rating):
        books_in_range = []
        curr = self.head
        while curr:
            if min_rating <= curr.rating <= max_rating:
                books_in_range.append(curr)
            curr = curr.next
        return books_in_range

    def find_by_price_range(self, min_price, max_price):
        books_in_range = []
        curr = self.head
        while curr:
            if min_price <= curr.price <= max_price:
                books_in_range.append(curr)
            curr = curr.next
        return books_in_range

# create some books
book1 = Book(1, "book1", "author1", 2000, 4.5)
book2 = Book(2, "book2", "author2", 1500, 4.2)

# create a bookstore to add books
bookstore = Bookstore()
bookstore.add_book(book1)
bookstore.add_book(book2)

# Example usage of Bookstore class methods
book_id = 1
found_book = bookstore.find_by_id(book_id)
if found_book:
    print(f"Title: {found_book.title}, Author: {found_book.author}")
else:
    print("Book not found.")

author_name = "author1"
books_by_author = bookstore.find_by_author(author_name)
print("\nBooks found by author:")
for book in books_by_author:
    print(f"Title: {book.title}, Author: {book.author}")

min_rating = 4.0
max_rating = 4.5
books_by_rating = bookstore.find_by_rating_range(min_rating, max_rating)
print("\nBooks found by rating range:")
for book in books_by_rating:
    print(f"Title: {book.title}, Rating: {book.rating}")

min_price = 1000
max_price = 2000
books_by_price = bookstore.find_by_price_range(min_price, max_price)
print("\nBooks found by price range:")
for book in books_by_price:
    print(f"Title: {book.title}, Price: ${book.price}")
