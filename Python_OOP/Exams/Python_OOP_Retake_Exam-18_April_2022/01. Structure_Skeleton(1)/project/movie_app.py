# from movie_specification.fantasy import Fantasy
# from movie_specification.thriller import Thriller
# from movie_specification.action import Action
from project.movie_specification.movie import Movie,exc
# from movie_specification.movie import Movie
from project.user import User
# from user import User

def _check_lists(function):
    def check(**kwargs):
        condition = kwargs.get("error_raise_condition",True)
        no_error = kwargs.get("do_not_raise_error", False)
        name = kwargs.get("name",True)
        attr1 = kwargs.get("attr1",name)
        name1 = kwargs.get("name1",name)
        att = kwargs.get("attr",name)
        excp = kwargs.get("exc",Exception)
        ob = [value for value in kwargs["collection"] if function(getattr(value, att, name),name) and function(getattr(value,attr1,name1),name1)]
        if condition:
            condition = bool(ob)
        else:
            condition = bool(not ob)
        if not no_error:
            exc(kwargs.get("error_message", ""),condition,excp)
        return ob[kwargs.get("item",0)] if ob else True
    return check

@_check_lists
def _check_collections(cond,val,op = "=="):
    if op == "==":
        return cond == val
    if op == "!=":
        return cond != val

class MovieApp:

    def __init__(self):
        self.__check_collections = _check_collections
        self.exc = exc
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        self.__check_collections(
            collection=self.users_collection,
            attr="username",name=username,
            error_message="User already exists!"
        )
        self.users_collection.append(User(username,age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        owner = self.__check_collections(
            collection=self.users_collection,
            name=username,attr="username",
            error_raise_condition=False, error_message="This user does not exist!"
        )
        if movie.owner.username != owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.__check_collections(
            collection = self.movies_collection,
            attr="title",name=movie.title,
            error_message="Movie already added to the collection!"
        )
        movie.owner = owner
        self.movies_collection.append(movie)
        owner.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, ** kwargs):
        self.__is_movie_uploaded(movie)
        user = self.__get_user(username)
        self.__is_the_user_owner(movie,user)
        for values in kwargs.items():
            movie.__setattr__(*values)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        self.__is_movie_uploaded(movie)
        user = self.__get_user(username)
        self.__is_the_user_owner(movie, user)
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__get_user(username)
        self.__is_movie_uploaded(movie)
        if self.__is_the_user_owner(movie,user,False):
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        self.__check_collections(
            collection=user.movies_liked,
            attr="title", name=movie.title,
            error_message=f"{username} already liked the movie {movie.title}!"
        )
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."


    def dislike_movie(self, username: str, movie: Movie):
        user = self.__get_user(username)
        self.__check_collections(
            collection=user.movies_liked,
            attr="title", name=movie.title,
            error_raise_condition=False,error_message=f"{username} has not liked the movie {movie.title}!"
        )
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        movies = sorted(self.movies_collection, key=lambda movie: (-movie.year,movie.title))
        return "\n".join(movie.details() for movie in movies)

    def __str__(self):
        all_users = ", ".join(user.username for user in self.users_collection) if self.users_collection else "No users."
        all_movies = ", ".join(movie.title for movie in self.movies_collection) if self.movies_collection else "No movies."
        return f"All users: {all_users}\n" + \
            f"All movies: {all_movies}"

    def __is_movie_uploaded(self, movie: Movie):
        self.__check_collections(
            collection=self.movies_collection,
            attr="title", name=movie.title,
            error_raise_condition=False, error_message=f"The movie {movie.title} is not uploaded!"
        )

    def __get_user(self, username):
        return self.__check_collections(
            collection=self.users_collection,
            attr="username", name=username,
            do_not_raise_error=True
        )

    def __is_the_user_owner(self,movie,user,exc=True):
        if movie.owner != user:
            if not exc:
                return False
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        return True

    # @staticmethod
    # def __check_lists(function):
    #     def check(**kwargs):
    #         condition = kwargs.get("error_raise_condition",True)
    #         no_error = kwargs.get("do_not_raise_error", False)
    #         name = kwargs.get("name",True)
    #         attr1 = kwargs.get("attr1",name)
    #         name1 = kwargs.get("name1",name)
    #         att = kwargs.get("attr",name)
    #         exc = kwargs.get("exc",Exception)
    #         ob = [value for value in kwargs["collection"] if function(getattr(value, att, name),name) and function(getattr(value,attr1,name1),name1)]
    #         if condition:
    #             condition = bool(ob)
    #         else:
    #             condition = bool(not ob)
    #         if not no_error:
    #             Fantasy.exc(kwargs.get("error_message", ""),condition,exc)
    #         return ob[kwargs.get("item",0)] if ob else True
    #     return check
    #
    # @staticmethod
    # @__check_lists
    # def __check_collections(cond,val,op = "=="):
    #     if op == "==":
    #         return cond == val
    #     if op == "!=":
    #         return cond != val