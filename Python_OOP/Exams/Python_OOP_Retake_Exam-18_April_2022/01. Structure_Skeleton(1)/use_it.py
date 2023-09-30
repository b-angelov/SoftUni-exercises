from project.movie_app import MovieApp
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.action import Action
from project.movie_specification.thriller import Thriller

movie_app = MovieApp()
print(movie_app.register_user('Martin', 24))
# print(movie_app.register_user('Martin', 24))
user = movie_app.users_collection[0]
movie = Action('Die Hard', 1988, user, 18)
print(movie_app.upload_movie('Martin', movie))
print(movie_app.movies_collection[0].title)
print(movie_app.register_user('Alexandra', 25))
user2 = movie_app.users_collection[1]
movie2 = Action('Free Guy', 2021, user2, 16)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.like_movie('Alexandra', movie))
print(movie_app.dislike_movie('Martin', movie2))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.delete_movie('Alexandra', movie2))
movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.display_movies())
print(movie_app)


###################MY TESTS########################

#movie_app

print(movie_app.register_user("Me",6))
# print(movie_app.register_user("Me",8))
Me = movie_app.users_collection[-1]
my_own_movie = Fantasy("My own movie, do not touch it!!!",1888,Me,841)
my_other_movie = Thriller("My other movie, do not watch it!!!",1888,Me,13)
print(movie_app.upload_movie("Me",my_own_movie))
# print(movie_app.upload_movie("Me",my_own_movie))

print(movie_app.edit_movie("Me",my_own_movie,title="Do not watch it!",year=1888,likes=8654112,age_restriction = 8))
print(movie_app.delete_movie("Me",my_own_movie))
print(movie_app.like_movie("Alexandra",my_own_movie))
print(movie_app.like_movie("Martin",my_own_movie))
print(movie_app.like_movie("Me",movie2))
# print(movie_app.like_movie("Alexandra",my_own_movie))
print(movie_app.movies_collection[-1].likes)
# print(movie_app.dislike_movie("Me",movie2))
# movie_app.movies_collection.clear()
# movie_app.users_collection.clear()
print(movie_app.display_movies())
print(movie_app)
movie2.owner = Me
print(movie_app.upload_movie("Me",my_other_movie))
print(movie_app.edit_movie("Me",my_other_movie,title="Do not watch it!",year=1948,likes=-221,age_restriction = 16))

print(movie_app.users_collection[-1])