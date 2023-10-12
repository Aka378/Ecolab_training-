import pyodbc as db

def add_author(args, cursor, connection):
    author_id, author_name = args
    cursor.execute("INSERT INTO Authors (ID, NAME) VALUES (?, ?)", (author_id, author_name))
    connection.commit()
    
def remove_author(args, cursor, connection):
    author_id = args[0]
    cursor.execute("DELETE FROM Authors WHERE ID=?", (author_id,))
    connection.commit()
    
def update_author(args, cursor, connection):
    author_id, new_name = args
    cursor.execute("UPDATE Authors SET NAME=? WHERE ID=?", (new_name, author_id))
    connection.commit()
   
def get_all_authors(args, cursor):
    cursor.execute("SELECT * FROM Authors")
    authors = cursor.fetchall()
    for author in authors:
        print(author)

def add_book(args, cursor, connection):
    book_id, title, author_id, price = args
    cursor.execute("INSERT INTO Books (ID, TITLE, AUTHOR_ID, PRICE) VALUES (?, ?, ?, ?)", (book_id, title, author_id, price))
    connection.commit()
    

def remove_book(args, cursor, connection):
    book_id = args[0]
    cursor.execute("DELETE FROM Books WHERE ID=?", (book_id,))
    connection.commit()
    

def update_book(args, cursor, connection):
    book_id, new_title, new_author_id, new_price = args
    cursor.execute("UPDATE Books SET TITLE=?, AUTHOR_ID=?, PRICE=? WHERE ID=?", (new_title, new_author_id, new_price, book_id))
    connection.commit()
    
def get_all_books(args, cursor):
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    for book in books:
        print(book)

def add_user(args, cursor, connection):
    user_id, user_name = args
    cursor.execute("INSERT INTO Users (ID, NAME) VALUES (?, ?)", (user_id, user_name))
    connection.commit()
    print(f"User '{user_name}' with ID {user_id} added successfully.")

def remove_user(args, cursor, connection):
    user_id = args[0]
    cursor.execute("DELETE FROM Users WHERE ID=?", (user_id,))
    connection.commit()
    print(f"User with ID {user_id} removed successfully.")

def update_user(args, cursor, connection):
    user_id, new_name = args
    cursor.execute("UPDATE Users SET NAME=? WHERE ID=?", (new_name, user_id))
    connection.commit()

def add_review(args, cursor, connection):
    book_id, user_id, rating, comment = args
    cursor.execute("INSERT INTO Reviews (BOOK_ID, USER_ID, RATING, COMMENT) VALUES (?, ?, ?, ?)", (book_id, user_id, rating, comment))
    connection.commit()

def remove_review(args, cursor, connection):
    review_id = args[0]
    cursor.execute("DELETE FROM Reviews WHERE ID=?", (review_id,))
    connection.commit()

def get_book_reviews(args, cursor):
    book_id = args[0]
    cursor.execute("SELECT * FROM Reviews WHERE BOOK_ID=?", (book_id,))
    reviews = cursor.fetchall()
    for review in reviews:
        print(review)

def main():
    driver = '{ODBC Driver 18 for SQL Server}'
    server = r'localhost\SQLEXPRESS'
    database = 'NEW_ECOLAB'
    encrypt = 'no'
    trusted_connection = 'yes'

    connection_string = f'''
        DRIVER={driver};
        SERVER={server};
        DATABASE={database};
        trusted_connection={trusted_connection};
        ENCRYPT={encrypt};
    '''

    print(connection_string)

    with db.connect(connection_string) as connection:
        print('Connection successful')
        cursor = connection.cursor()

        commands = {
            "add-author": add_author,
            "remove-author": remove_author,
            "update-author": update_author,
            "get-all-authors": get_all_authors,
            "add-book": add_book,
            "remove-book": remove_book,
            "update-book": update_book,
            "get-all-books": get_all_books,
            "add-user": add_user,
            "remove-user": remove_user,
            "update-user": update_user,
            "add-review": add_review,
            "remove-review": remove_review,
            "get-book-reviews": get_book_reviews,
        }

        while True:
            user_input = input().split()
            command_name = user_input[0]
            command_args = user_input[1:]

            if command_name in commands:
                try:
                    commands[command_name](command_args, cursor, connection)
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Invalid command. Please try again.")

if __name__ == "_main_":
    main()