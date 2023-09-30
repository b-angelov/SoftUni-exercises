from unittest import TestCase
from project.bookstore import Bookstore


class TestBookstore(TestCase):

    def setUp(self):
        self.store = Bookstore(1841)

    def test_init(self):
        self.assertEqual(self.store.books_limit, 1841)
        self.assertEqual(self.store.availability_in_store_by_book_titles, {})

    def test_total_sold_books(self):
        self.assertEqual(self.store.total_sold_books, 0)
        self.assertRaises(Exception, self.store.total_sold_books, 8)

    def test_books_limit_valid(self):
        self.store.books_limit += 1
        self.assertEqual(self.store.books_limit, 1842)

    def test_books_limit_invalid(self):
        with self.assertRaises(Exception) as msg:
            self.store.books_limit = 0
        self.assertEqual(str(msg.exception), "Books limit of 0 is not valid")

    def test_receive_book_valid(self):
        self.assertEqual(self.store.receive_book("The Lord of The Rings",211), f"211 copies of The Lord of The Rings are available in the bookstore.")
        self.assertEqual(self.store.availability_in_store_by_book_titles["The Lord of The Rings"], 211)
        self.assertEqual(self.store.receive_book("The Lord of The Rings",4), f"215 copies of The Lord of The Rings are available in the bookstore.")
        self.assertEqual(self.store.availability_in_store_by_book_titles["The Lord of The Rings"], 215)


    def test_receive_book_invalid(self):
        self.store.receive_book("The Lord of The Rings",1838)
        with self.assertRaises(Exception) as msg:
            self.store.receive_book("The Lord of The Rings", 4)
        self.assertEqual(str(msg.exception), "Books limit is reached. Cannot receive more books!")


    def test_sell_book_valid(self):
        self.store.receive_book("The Lord of The Rings", 1838)
        self.store.receive_book("The Hobbit", 3)
        self.assertEqual(self.store.sell_book("The Lord of The Rings",20),"Sold 20 copies of The Lord of The Rings")
        self.assertEqual(self.store.availability_in_store_by_book_titles["The Lord of The Rings"],1818)
        self.assertEqual(self.store.total_sold_books,20)

    def test_sell_book_invalid(self):
        with self.assertRaises(Exception) as msg:
            self.store.sell_book("Misty Mountains", 155)
        self.assertEqual(str(msg.exception),f"Book Misty Mountains doesn't exist!")
        self.store.receive_book("Misty Mountains", 184)
        with self.assertRaises(Exception) as msg:
            self.store.sell_book("Misty Mountains", 185)
        self.assertEqual(str(msg.exception),"Misty Mountains has not enough copies to sell. Left: 184")



    def test_len(self):
        self.store.receive_book("The Lord of The Rings", 70)
        self.store.receive_book("The Hobbit", 70)
        self.store.receive_book("Misty Mountains", 7)
        self.assertEqual(len(self.store), 147)


    def test_str(self):
        self.store.receive_book("The Lord of The Rings",100)
        self.store.receive_book("The Hobbit",10)
        self.store.receive_book("Misty Mountains",5)
        self.store.sell_book("The Lord of The Rings", 88)
        self.store.sell_book("The Hobbit", 10)
        self.store.sell_book("Misty Mountains", 1)
        self.assertEqual(str(self.store), """Total sold books: 99
Current availability: 16
 - The Lord of The Rings: 12 copies
 - The Hobbit: 0 copies
 - Misty Mountains: 4 copies""")
