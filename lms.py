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


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book_id, title, author, total_copies):
        for b in self.books:
            if b.id == book_id:
                print("Error: Book ID already exists.")
                return
        book = Book(book_id, title, author, total_copies)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def add_member(self, member_id, name, email):
        for m in self.members:
            if m.id == member_id:
                print("Error: Member ID already exists.")
                return
        member = Member(member_id, name, email)
        self.members.append(member)
        print(f"Member '{name}' registered successfully!")

    def find_book(self, book_id):
        for b in self.books:
            if b.id == book_id:
                return b
        return None

    def find_member(self, member_id):
        for m in self.members:
            if m.id == member_id:
                return m
        return None

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if not member:
            print("Error: Member not found!")
            return False
        if not book:
            print("Error: Book not found!")
            return False
        return member.borrow_book(book)

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if not member or not book:
            print("Error: Member or book not found!")
            return False
        return member.return_book(book)

    def display_available_books(self):
        print("\n=== Available Books ===")
        for b in self.books:
            if b.available_copies > 0:
                print(f"{b.title} by {b.author} - {b.available_copies} copies available")

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        member.display_borrowed_books()


if __name__ == "__main__":
    print("=" * 60)
    print("TESTING FULL LIBRARY SYSTEM (BOOK + MEMBER + LIBRARY)")
    print("=" * 60)

    library = Library()

    print("\n--- Adding Books ---")
    library.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    library.add_book(2, "Clean Code", "Robert Martin", 2)
    library.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    library.add_book(4, "Design Patterns", "Gang of Four", 2)

    print("\n--- Adding Members ---")
    library.add_member(101, "Alice Smith", "alice@email.com")
    library.add_member(102, "Bob Jones", "bob@email.com")
    library.add_member(103, "Carol White", "carol@email.com")

    print("\n--- Display Available Books ---")
    library.display_available_books()

    print("\n--- Borrowing Books ---")
    library.borrow_book(101, 1)
    library.borrow_book(101, 2)
    library.borrow_book(102, 1)

    print("\n--- Display Member Books ---")
    library.display_member_books(101)
    library.display_member_books(102)
    library.display_member_books(103)

    print("\n--- Display Available Books After Borrowing ---")
    library.display_available_books()

    print("\n--- Borrowing Last Copy ---")
    library.borrow_book(103, 3)
    library.display_available_books()

    print("\n--- Attempting to Borrow Unavailable Book ---")
    library.borrow_book(102, 3)

    print("\n--- Testing Borrowing Limit ---")
    library.borrow_book(101, 4)
    library.display_member_books(101)
    library.borrow_book(101, 3)

    print("\n--- Returning Books ---")
    library.return_book(101, 1)
    library.return_book(102, 1)
    library.display_member_books(101)
    library.display_available_books()

    print("\n--- Attempting Invalid Return ---")
    library.return_book(102, 2)

    print("\n--- Return and Re-borrow ---")
    library.return_book(103, 3)
    library.borrow_book(102, 3)
    library.display_member_books(102)

    print("\n--- Error Handling ---")
    library.borrow_book(999, 1)
    library.borrow_book(101, 999)
    library.return_book(999, 1)
    library.display_member_books(999)

    print("\n--- Final Available Books ---")
    library.display_available_books()

    print("\n" + "=" * 60)
    print("LIBRARY CLASS TEST COMPLETE")
    print("=" * 60)
