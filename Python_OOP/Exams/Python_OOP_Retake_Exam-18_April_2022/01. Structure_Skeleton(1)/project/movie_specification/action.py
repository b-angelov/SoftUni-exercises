# from movie_specification.movie import Movie
from project.movie_specification.movie import Movie

class Action(Movie):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 12):
        super().__init__(title, year, owner, age_restriction)
        self._age_restrict_message = "Action movies must be restricted for audience under 12 years!"
        self.genre_age_restriction = 12
        self.age_restriction = age_restriction

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"
