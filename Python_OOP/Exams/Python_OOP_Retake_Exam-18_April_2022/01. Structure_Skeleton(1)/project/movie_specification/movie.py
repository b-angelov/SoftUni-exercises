from abc import ABC, abstractmethod
# from user import User
from project.user import User


def raise_exception(function):
    def e_raise(message, condition, error=ValueError):
        if function(condition):
            raise error(message)

    return e_raise


@raise_exception
def exc(cond):
    if cond: return True

class Movie(ABC):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.exc = exc
        self.title = title
        self.year = year
        self.owner = owner
        self._age_restrict_message = "Action movies must be restricted for audience under 12 years!"
        self.genre_age_restriction = 0
        self.age_restriction = age_restriction
        self.likes = 0

    @abstractmethod
    def details(self):
        """It returns a string with information about the movie by its type."""
        ...

    # @staticmethod
    # def raise_exception(function):
    #     def e_raise(message, condition, error=ValueError):
    #         if function(condition):
    #             raise error(message)
    #
    #     return e_raise
    #
    # @staticmethod
    # @raise_exception
    # def exc(cond):
    #     if cond: return True

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self.exc("The title cannot be empty string!",not title)
        self._title = title

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, year: int):
        self.exc("Movies weren't made before 1888!",year < 1888)
        self._year = year

    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, owner: User):
        self.exc("The owner must be an object of type User!",type(owner) != User)
        self._owner = owner

    @property
    def age_restriction(self):
        return self._age_restriction
    @age_restriction.setter
    def age_restriction(self, value: int):
        # try:
        #     self._age_restriction
        # except:
        #     self._age_restriction = 0
        self.exc(self._age_restrict_message, value < self.genre_age_restriction)
        self._age_restriction = value





