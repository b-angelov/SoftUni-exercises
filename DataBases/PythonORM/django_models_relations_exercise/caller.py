import os
from datetime import timedelta, date

import django
from django.db.models import Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Artist, Song, Product, Review, Driver, DrivingLicense, Owner, Registration, \
    Car


# Create queries within functions

# TASK 1
def show_all_authors_with_their_books():
    return '\n'.join(
        filter(lambda x: x, [(
                                 f'{author.name} has written - {", ".join(book.title for book in author.book_set.all())}!' if author.book_set.count() else '')
                             for author in
                             Author.objects.all()])
    )


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    return Song.objects.filter(artists__name=artist_name).order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    return Product.objects.get(name=product_name).reviews.aggregate(Avg('rating'))['rating__avg']


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()

def calculate_licenses_expiration_dates():
    return '\n'.join(
        f'License with number: {driving_license.license_number} expires on {driving_license.issue_date + timedelta(days=365)}!'
        for driving_license in
        DrivingLicense.objects.all().order_by('-license_number')
    )


def get_drivers_with_expired_licenses(due_date: date):
    return Driver.objects.annotate(expiration_date=F('license__issue_date') + timedelta(days=365)).filter(expiration_date__gt=due_date)


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    registration.registration_date = date.today()
    car = Car.objects.filter(registration__registration_number__isnull=True).first()
    car.owner = owner
    registration.car = car
    owner.cars.add(car)
    registration.save()
    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."


if __name__ == '__main__':
    Registration.objects.all().delete()
    Car.objects.all().delete()
    Owner.objects.all().delete()
    # Create owners
    owner1 = Owner.objects.create(name='Ivelin Milchev')
    owner2 = Owner.objects.create(name='Alice Smith')

    # Create cars
    car1 = Car.objects.create(model='Citroen C5', year=2004)
    car2 = Car.objects.create(model='Honda Civic', year=2021)
    # Create instances of the Registration model for the cars
    registration1 = Registration.objects.create(registration_number='TX0044XA')
    registration2 = Registration.objects.create(registration_number='XYZ789')

    print(register_car_by_owner(owner1))

