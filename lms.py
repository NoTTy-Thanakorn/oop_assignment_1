class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow_copy(self):
        if self.available_copies <= 0:
            print(f"Error: '{self.title}' is currently unavailable!")
            return False
        self.available_copies -= 1
        print(f"A copy of '{self.title}' has been borrowed.")
        return True

    def return_copy(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print(f"A copy of '{self.title}' has been returned.")
            return True
        else:
            print(f"Error: All copies of '{self.title}' are already in the library.")
            return False

    def display_info(self):
        print(f"Book ID: {self.id} | Title: {self.title} | Author: {self.author} "
              f"| Available: {self.available_copies}/{self.total_copies}")


if __name__ == "__main__":
    print("=" * 60)
    print("TESTING BOOK CLASS")
    print("=" * 60)

    book1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
    book2 = Book(2, "Clean Code", "Robert Martin", 2)
    book3 = Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)

    print("\n--- Displaying All Books ---")
    book1.display_info()
    book2.display_info()
    book3.display_info()

    print("\n--- Borrowing Copies ---")
    book1.borrow_copy()
    book1.borrow_copy()
    book1.display_info()

    print("\n--- Borrowing Until Unavailable ---")
    book1.borrow_copy()
    book1.borrow_copy()

    print("\n--- Returning Copies ---")
    book1.return_copy()
    book1.return_copy()
    book1.return_copy()

    print("\n--- Borrowing and Returning Another Book ---")
    book2.borrow_copy()
    book2.display_info()
    book2.return_copy()
    book2.display_info()

    print("\n--- Final Status of All Books ---")
    book1.display_info()
    book2.display_info()
    book3.display_info()

    print("\n" + "=" * 60)
    print("BOOK CLASS TEST COMPLETE")
    print("=" * 60)
