
class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    def __str__(self):
        liked_movies = '\n'.join(movie.details() for movie in self.movies_liked) if self.movies_liked else 'No movies liked.'
        owned_movies = '\n'.join(movie.details() for movie in self.movies_owned) if self.movies_owned else 'No movies owned.'
        return f"Username: {self.username}, Age: {self.age}\n" +\
        "Liked movies:\n" +\
        f"{liked_movies}\n" +\
        "Owned movies:\n" +\
        f"{owned_movies}"

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        if not username:
            raise ValueError("Invalid username!")
        self.__username = username

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = age