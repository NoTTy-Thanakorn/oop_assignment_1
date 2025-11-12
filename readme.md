# Library Management System - OOP Version

## Project Overview
This project is a Library Management System refactored from a procedural style to an Object-Oriented Programming (OOP) design in Python. It allows managing books, members, borrowing and returning books while enforcing rules like borrowing limits and availability checks.

## Project Structure
oop_ass_1/
├── procedural_version/
│   ├── library_procedural.py
│   └── test_procedural.py
├── oop_solution/
│   ├── lsm.py               # OOP implementation (Book, Member, Library)
│   └── test_oop.py          # Test suite for OOP version

## Design Overview
### Book Class
- Attributes: 
  - id: unique book identifier
  - title: book title
  - author: book author
  - total_copies: total copies of the book
  - available_copies: copies currently available
- Methods:
  - borrow(): decreases available_copies by 1 if available
  - return_book(): increases available_copies by 1

### Member Class
- Attributes:
  - id: unique member identifier
  - name: member name
  - email: member email
  - borrowed_books: list of borrowed book IDs
- Methods:
  - borrow_book(book_id): adds book ID to borrowed_books if limit not exceeded
  - return_book(book_id): removes book ID from borrowed_books

### Library Class
- Attributes:
  - books: list of Book objects
  - members: list of Member objects
- Methods:
  - add_book(id, title, author, total_copies): add a book to library
  - add_member(id, name, email): register a new member
  - borrow_book(member_id, book_id): process borrowing
  - return_book(member_id, book_id): process returning
  - display_available_books(): list all books with available copies
  - display_member_books(member_id): list books borrowed by a member

## Testing
### Test Coverage
- Basic Operations:
  - Adding books and members
  - Borrowing and returning books
  - Displaying available books
  - Displaying a member's borrowed books
- Edge Cases:
  - Borrowing unavailable books
  - Borrowing beyond the limit (3 books per member)
  - Returning books not borrowed
  - Handling non-existent books or members

### How to Run Tests
Open terminal, navigate to `oop_ass_1/oop_solution/` folder and run:

