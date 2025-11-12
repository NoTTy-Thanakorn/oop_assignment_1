from lms import Library


def test_library_system():
    library = Library()

    library.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    library.add_book(2, "Clean Code", "Robert Martin", 2)
    library.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    library.add_book(4, "Design Patterns", "Gang of Four", 2)

    library.add_member(101, "Alice Smith", "alice@email.com")
    library.add_member(102, "Bob Jones", "bob@email.com")
    library.add_member(103, "Carol White", "carol@email.com")

    library.display_available_books()

    library.borrow_book(101, 1)
    library.borrow_book(101, 2)
    library.borrow_book(102, 1)

    library.display_member_books(101)
    library.display_member_books(102)
    library.display_member_books(103)

    library.display_available_books()

    library.borrow_book(103, 3)
    library.display_available_books()

    library.borrow_book(102, 3)

    library.borrow_book(101, 4)
    library.display_member_books(101)
    library.borrow_book(101, 3)

    library.return_book(101, 1)
    library.return_book(102, 1)
    library.display_member_books(101)
    library.display_available_books()

    library.return_book(102, 2)

    library.return_book(103, 3)
    library.borrow_book(102, 3)
    library.display_member_books(102)

    library.borrow_book(999, 1)
    library.borrow_book(101, 999)
    library.return_book(999, 1)
    library.display_member_books(999)

    library.display_available_books()


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING OOP LIBRARY SYSTEM TEST SUITE")
    print("=" * 60)
    test_library_system()
    print("=" * 60)
    print("OOP LIBRARY SYSTEM TEST COMPLETE")
    print("=" * 60)
