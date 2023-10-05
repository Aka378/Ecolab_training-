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
book1 = Book(1, "A river sutra", "Gita mehta", 2000, 4.5)
book2 = Book(2, "A sense of time", "H.S.vatsyan", 1500, 4.2)
book3 = Book(3, "An equal music", "Gita mehta", 2000, 4.5)
book4 = Book(4, "Amar kosh", "Amar singh", 1500, 4.2)

# create a bookstore to add books
bookstore = Bookstore()
bookstore.add_book(book1)
bookstore.add_book(book2)
bookstore.add_book(book3)
bookstore.add_book(book4)
# Example usage of Bookstore class methods
print("books found:")
Find_by_id=bookstore.find_by_id(1)
print(Find_by_id.author,Find_by_id.title)

print("\nbooks found by author:")    
Find_by_author=bookstore.find_by_author("Gita mehta")
for i in Find_by_author:
    print(i.title)

print("\nbooks found by rating:")
Find_by_rating=bookstore.find_by_rating_range(4.0,4.5)
for i in Find_by_rating:
    print(i.title)

print("\nbooks found by price:")
Find_by_price=bookstore.find_by_price_range(1000,2500)
for i in Find_by_price:
    print(i.title)
