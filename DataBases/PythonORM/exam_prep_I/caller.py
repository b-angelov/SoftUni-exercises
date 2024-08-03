import os
import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create queries within functions
def get_directors(search_name=None, search_nationality=None):
    search = dict(filter(lambda x: x[1],{
        "full_name__icontains": search_name,
        "nationality__icontains": search_nationality
    }.items()))
    return '\n'.join(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}" for d in Director.objects.filter(**search).order_by('full_name')) or ""




def get_top_director():
    best_director = Director.objects.get_directors_by_movies_count().first()
    return f"Top Director: {best_director.full_name}, movies: {best_director.movies_count}." if best_director else ""


def get_top_actor():
    top_actor = Actor.objects.prefetch_related('movies').annotate(movies_starred=Count('movies')).annotate(average_rating=Avg('movies__rating')).order_by('-movies_starred', "full_name").first()
    return f"Top Actor: {top_actor.full_name}, starring in movies: {', '.join(m.title for m in top_actor.movies.all())}, movies average rating: {top_actor.average_rating:.1f}" if top_actor and top_actor.movies.count() else ""



def get_actors_by_movies_count():
    top_actors = Actor.objects.annotate(count_participations=Count('movie')).filter(count_participations__gt=0).order_by('-count_participations', 'full_name')[:3]
    return '\n'.join(f"{a.full_name}, participated in {a.count_participations} movies" for a in top_actors) if top_actors else ""


def get_top_rated_awarded_movie():
    top_movie = Movie.objects.select_related('starring_actor').prefetch_related("actors").filter(is_awarded=True).order_by('-rating','title').first()
    return f"Top rated awarded movie: {top_movie.title}, rating: {top_movie.rating:.1f}. Starring actor: {top_movie.starring_actor.full_name if top_movie.starring_actor else 'N/A'}. Cast: {', '.join(a.full_name for a in top_movie.actors.all().order_by('full_name'))}." if top_movie else ""


def increase_rating():
    updated = Movie.objects.filter(is_classic=True, rating__lte=9.9).update(rating=F('rating') + 0.1)
    return f"Rating increased for {updated} movies." if updated else "No ratings increased."





if __name__ == '__main__':
    pass
    # print(Director.objects.get_directors_by_movies_count())
    # print(get_directors(None, 'zear'))
    # print(get_top_director())
    # print(get_top_actor())
    # print(get_actors_by_movies_count())
    # print(get_top_rated_awarded_movie())
    print(increase_rating())