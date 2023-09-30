# from movie_specification.movie import Movie
from project.movie_specification.movie import Movie

class Thriller(Movie):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 16):
        super().__init__(title, year, owner, age_restriction)
        self._age_restrict_message = "Thriller movies must be restricted for audience under 16 years!"
        self.genre_age_restriction = 16
        self.age_restriction = age_restriction

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"