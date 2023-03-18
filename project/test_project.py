from project import borrow_book
from project import list_books
from project import return_book
def test_list_books():
    assert list_books(["book1", "book2", "book3"]) == "AVAILABLE BOOKS ARE:\nbook1\nbook2\nbook3\n"

def test_borrow_book():
    books = ["book1", "book2", "book3"]
    borrower = "John"
    book_to_borrow = "book2"
    expected_track = [{"John": "book2"}]
    expected_books = ["book1", "book3"]
    track = []
    borrow_book(books, borrower, book_to_borrow, track)
    assert track == expected_track
    assert books == expected_books

def test_return_book():
    books = ["book1", "book2", "book3"]
    borrower = "John"
    book_to_return = "book2"
    track = [{"John": "book2"}]
    expected_books = ["book1", "book2", "book3"]
    return_book(books, borrower, book_to_return, track)
    assert books == expected_books
