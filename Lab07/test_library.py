import unittest
from unittest.mock import Mock
from library import Library
from library_repository import LibraryRepository

class LibraryTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = Mock(spec=LibraryRepository)
        self.library = Library(self.repo)

    def test_borrow_book_success(self):
        self.repo.remove_book.return_value = True
        result = self.library.borrow_book("1984")
        self.assertTrue(result)
        self.repo.remove_book.assert_called_once_with("1984")

    def test_return_book(self):
        self.library.return_book("Dune", "Herbert", 1965)
        self.repo.add_book.assert_called_once_with("Dune", "Herbert", 1965)

    def test_list_books(self):
        self.repo.get_all_books.return_value = ["Book A", "Book B"]
        result = self.library.list_books()
        self.assertEqual(result, ["Book A", "Book B"])
        self.repo.get_all_books.assert_called_once()

if __name__ == "__main__":
    unittest.main()
