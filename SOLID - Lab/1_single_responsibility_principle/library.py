# Refactor the provided code, so there is a separate class called Library, which contains books and has a method called find_book(title) that returns the book with
# the given title. Remove the unnecessary code from the Book class.


from single_responsibility_principle.book import Book

class Library:

    def __init__(self) -> None:
        self.books = []

    def find_book(self, book: Book) -> Book:
        try:
            found_book = next(b for b in self.books if b.title == book.title)
            return found_book
        except StopIteration:
            pass
