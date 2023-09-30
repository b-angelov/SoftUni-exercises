import unittest
from project.movie import Movie


class TestsMovieClass(unittest.TestCase):
    def test_init_should_create_correct_attr(self):
        a = Movie("Dune", 2021, 8.5)
        self.assertEqual(a.name, "Dune")
        self.assertEqual(a.year, 2021)
        self.assertEqual(a.rating, 8.5)
        self.assertEqual(a.actors, [])

    def test_wrong_init_should_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            Movie("", 2021, 8.5)
        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")
        with self.assertRaises(ValueError) as ve:
            Movie("Dune", 120, 8.5)
        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_actor(self):
        a = Movie("Dune", 2021, 8.5)
        a.add_actor("Zendaya")
        a.add_actor("Rebecca Ferguson")
        self.assertEqual(a.actors, ["Zendaya", "Rebecca Ferguson"])
        result = a.add_actor("Rebecca Ferguson")
        self.assertEqual(result, "Rebecca Ferguson is already added in the list of actors!")

    def test_gt_method(self):
        a = Movie("Dune", 2021, 8.5)
        b = Movie("Titanic", 1997, 7.8)
        result = str(a > b)
        self.assertEqual(result, '"Dune" is better than "Titanic"')
        c = Movie("The Shawshank Redemption", 1994, 9.2)
        second_result = str(a > c)
        self.assertEqual(second_result, '"The Shawshank Redemption" is better than "Dune"')

    def test_repr_method(self):
        a = Movie("Dune", 2021, 8.5)
        a.add_actor("Zendaya")
        a.add_actor("Rebecca Ferguson")
        self.assertEqual(str(a), "Name: Dune\nYear of Release: 2021\nRating: 8.50\nCast: Zendaya, Rebecca Ferguson")


if __name__ == "__main__":
    unittest.main()
