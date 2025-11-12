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


class Member:
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print(f"Error: {self.name} has reached the borrowing limit (3 books).")
            return False
        if book.borrow_copy():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
            return True
        return False

    def return_book(self, book):
        if book not in self.borrowed_books:
            print(f"Error: {self.name} has not borrowed '{book.title}'.")
            return False
        if book.return_copy():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
            return True
        return False

    def display_borrowed_books(self):
        print(f"\nBooks borrowed by {self.name}:")
        if not self.borrowed_books:
            print("  No books currently borrowed.")
        else:
            for b in self.borrowed_books:
                print(f"  - {b.title} by {b.author}")


if __name__ == "__main__":
    print("=" * 60)
    print("TESTING BOOK AND MEMBER CLASSES")
    print("=" * 60)

    book1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
    book2 = Book(2, "Clean Code", "Robert Martin", 2)
    book3 = Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)

    member1 = Member(101, "Alice Smith", "alice@email.com")
    member2 = Member(102, "Bob Jones", "bob@email.com")

    print("\n--- Display Initial Books ---")
    book1.display_info()
    book2.display_info()
    book3.display_info()

    print("\n--- Borrowing Books ---")
    member1.borrow_book(book1)
    member1.borrow_book(book2)
    member2.borrow_book(book1)
    member1.display_borrowed_books()
    member2.display_borrowed_books()

    print("\n--- Borrowing Limit Test ---")
    member1.borrow_book(book3)
    extra_book = Book(4, "Design Patterns", "Gang of Four", 1)
    member1.borrow_book(extra_book)

    print("\n--- Returning Books ---")
    member1.return_book(book1)
    member2.return_book(book1)
    member1.display_borrowed_books()
    member2.display_borrowed_books()

    print("\n--- Invalid Return ---")
    member2.return_book(book2)

    print("\n--- Final Status ---")
    book1.display_info()
    book2.display_info()
    book3.display_info()
    extra_book.display_info()

    print("\n" + "=" * 60)
    print("MEMBER CLASS TEST COMPLETE")
    print("=" * 60)
