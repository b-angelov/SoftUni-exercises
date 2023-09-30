from unittest import TestCase

from project.movie import Movie


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("Jewel In The Palace",2003,100.00)

    def test_init(self):
        self.assertEqual(self.movie.name, "Jewel In The Palace")
        self.assertEqual(self.movie.year, 2003)
        self.assertEqual(self.movie.rating, 100.00)
        self.assertEqual(self.movie.actors, [])


    def test_name_valid(self):
        self.assertEqual(self.movie.name,"Jewel In The Palace")
        self.movie.name = "A Jewel In The Palace"
        self.assertEqual(self.movie.name, "A Jewel In The Palace")

    def test_name_invalid(self):
        with self.assertRaises(Exception) as msg:
            self.movie.name = ""
        self.assertEqual(str(msg.exception), "Name cannot be an empty string!")

    def test_year_valid(self):
        self.assertEqual(self.movie.year, 2003)
        self.movie.year = 1887
        self.assertEqual(self.movie.year, 1887)

    def test_year_invalid(self):
        with self.assertRaises(Exception) as msg:
            self.movie.year = 1886
        self.assertEqual(str(msg.exception), "Year is not valid!")

    def test_add_actor_valid(self):
        self.assertEqual(self.movie.add_actor("Lee Young Eh"), None)
        self.assertIn("Lee Young Eh", self.movie.actors)
        self.movie.add_actor("Ji Jing Lee")
        self.assertEqual(self.movie.actors,["Lee Young Eh","Ji Jing Lee"])

    def test_add_actor_invalid(self):
        self.assertEqual(self.movie.add_actor("Lee Young Eh"), None)
        self.assertEqual(self.movie.add_actor("Lee Young Eh"), f"Lee Young Eh is already added in the list of actors!")

    def test_gt(self):
        new_movie = Movie("The Best Movie", 2222, 99)
        self.assertEqual(str(self.movie > new_movie),f"\"{self.movie.name}\" is better than \"{new_movie.name}\"")
        new_movie.rating = 101
        self.assertEqual(str(self.movie > new_movie),f"\"{new_movie.name}\" is better than \"{self.movie.name}\"")

    def test_repr(self):
        self.movie.add_actor("Lee Young Eh")
        self.movie.add_actor("Ji Jing Lee")
        self.assertEqual(str(self.movie), """Name: Jewel In The Palace
Year of Release: 2003
Rating: 100.00
Cast: Lee Young Eh, Ji Jing Lee""")