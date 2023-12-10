# Library Management System

# Define dictionaries to store books and users
books = {}
users = {}

# Function to add a book
def add_book(title, author, genre):
  book_id = len(books) + 1
  books[book_id] = {
    "title": title,
    "author": author,
    "genre": genre,
    "is_available": True
  }
  print(f"Book '{title}' added successfully with ID: {book_id}")

# Function to add a user
def add_user(name, email):
  user_id = len(users) + 1
  users[user_id] = {
    "name": name,
    "email": email,
    "books_borrowed": {}
  }
  print(f"User '{name}' added successfully with ID: {user_id}")

# Function to issue a book
def issue_book(book_id, user_id):
  if book_id not in books or not books[book_id]["is_available"]:
    print("Error: Book not available.")
    return
  if user_id not in users:
    print("Error: Invalid user ID.")
    return
  books[book_id]["is_available"] = False
  users[user_id]["books_borrowed"][book_id] = books[book_id]
  print(f"Book '{books[book_id]['title']}' issued to user '{users[user_id]['name']}' successfully.")

# Function to return a book
def return_book(book_id, user_id):
  if book_id not in books:
    print("Error: Invalid book ID.")
    return
  if user_id not in users or book_id not in users[user_id]["books_borrowed"]:
    print("Error: Book not borrowed by this user.")
    return
  books[book_id]["is_available"] = True
  del users[user_id]["books_borrowed"][book_id]
  print(f"Book '{books[book_id]['title']}' returned by user '{users[user_id]['name']}' successfully.")

# Main menu
while True:
  print("""
  Library Management System
  1. Add Book
  2. Add User
  3. Issue Book
  4. Return Book
  5. List Books
  6. List Users
  7. Quit
  """)
  choice = input("Enter your choice: ")
  if choice == "1":
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    add_book(title, author, genre)
  elif choice == "2":
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    add_user(name, email)
  elif choice == "3":
    book_id = int(input("Enter book ID: "))
    user_id = int(input("Enter user ID: "))
    issue_book(book_id, user_id)
  elif choice == "4":
    book_id = int(input("Enter book ID: "))
    user_id = int(input("Enter user ID: "))
    return_book(book_id, user_id)
  elif choice == "5":
    for book_id, book_details in books.items():
      print(f"Book ID: {book_id}")
      print(f"Title: {book_details['title']}")
      print(f"Author: {book_details['author']}")
      print(f"Genre: {book_details['genre']}")
      print(f"Available: {'Yes' if book_details['is_available'] else 'No'}")
      print("---")
  elif choice == "6":
    for user_id, user_details in users.items():
      print(f"User ID: {user_id}")
      print(f"Name: {user_details['name']}")
      print(f"Email: {user_details['email']}")
      print(f"Books Borrowed:")
      for borrowed_book_id, borrowed_book_details in user_details["books_borrowed"].items():
        print(f"- {borrowed_book_details['title']}")
