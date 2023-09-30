from unittest import TestCase

from project.library import Library


class TestLibrary(TestCase):

    def setUp(self) -> None:
        self.library = Library("Biblioteka")

    def test_init(self):
        self.assertEqual(self.library.name, "Biblioteka")
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})

    def test_name_valid(self):
        self.library.name = "Some other name"
        self.assertEqual(self.library.name, "Some other name")

    def test_name_invalid(self):
        with self.assertRaises(ValueError) as msg:
            self.library.name = ''
        self.assertEqual(str(msg.exception), "Name cannot be empty string!")
        self.assertEqual(self.library.name, "Biblioteka")

    def test_add_book(self):
        self.library.add_book("Tolkien", "The Lord of The Rings")
        self.library.add_book("Tolkien", "The Lord of The Rings")
        self.library.add_book("Tolkien", "Hobbit")
        self.assertEqual(self.library.books_by_authors, {"Tolkien": ["The Lord of The Rings", "Hobbit"]})

    def test_add_reader(self):
        self.assertEqual(self.library.add_reader("Bilbo"), None)
        self.assertIn("Bilbo", self.library.readers)
        self.assertEqual(self.library.add_reader("Bilbo"), f"Bilbo is already registered in the Biblioteka library.")

    def test_rent_book_valid(self):
        self.library.add_book("Tolkien", "The Lord of The Rings")
        self.library.add_book("Tolkien", "The Lord of The Rings")
        self.library.add_book("Tolkien", "Hobbit")
        self.library.add_book("Minor Author", "My first book")
        self.library.add_reader("Bilbo")
        self.assertEqual(self.library.rent_book("Bilbo","Tolkien","Hobbit"), None)
        self.assertNotIn("Hobbit", self.library.books_by_authors["Tolkien"])
        self.assertEqual(self.library.readers["Bilbo"], [{"Tolkien":"Hobbit"}])

    def test_rent_book_invalid(self):
        self.library.add_book("Tolkien", "The Lord of The Rings")
        self.library.add_book("Tolkien", "The Lord of The Rings")
        self.library.add_book("Tolkien", "Hobbit")
        self.library.add_book("Minor Author", "My first book")
        self.library.add_reader("Bilbo")
        self.assertEqual(self.library.rent_book("Rolly","Colly","Wolly"), f"Rolly is not registered in the Biblioteka Library.")
        self.assertEqual(self.library.rent_book("Bilbo","Colly","Wolly"), "Biblioteka Library does not have any Colly's books.")
        self.assertEqual(self.library.rent_book("Bilbo","Tolkien","Wolly"), """Biblioteka Library does not have Tolkien's "Wolly".""")

