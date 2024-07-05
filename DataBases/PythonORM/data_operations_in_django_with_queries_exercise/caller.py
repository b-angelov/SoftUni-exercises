import os
from decimal import Decimal
from math import ceil, floor

import django
from django.db.models import F
from unicodedata import decimal

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Car, Task, HotelRoom, Character
from main_app.models import Artifact
from main_app.models import Location


# Create queries within functions

# TASK 1

def create_pet(name: str, species: str):
    pet = Pet.objects.create(name=name, species=species)
    pet.save()
    return f"{name} is a very cute {species}!"


# TASK 2

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(name=name, origin=origin, age=age, description=description,
                                       is_magical=is_magical)
    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.age > 250 and artifact.is_magical:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


# TASK 3

def show_all_locations():
    return '\n'.join(
        f'{l.name} has a population of {l.population}!'
        for l in Location.objects.all().order_by('-pk')
    )


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    Location.objects.first().delete()


# TASK 4

def apply_discount():
    cars = Car.objects.all()
    for car in cars:
        car.price_with_discount = car.price * Decimal(1 - (sum(int(d) for d in str(car.year)) / 100))
    cars.bulk_update(cars, ['price_with_discount'])


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values("model", 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


# TASK 5

def show_unfinished_tasks():
    return '\n'.join(
        f"Task - {task['title']} needs to be done until {task['due_date']}!"
        for task in
        Task.objects.filter(is_finished=False).values("title", "due_date")
    )


def complete_odd_tasks():
    tasks = Task.objects.all()
    for task in tasks:
        if task.id % 2:
            task.is_finished = True
    Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str):
    Task.objects.filter(title=task_title).update(description=''.join(chr(ord(c) - 3) for c in text))


# TASK 6

def get_deluxe_rooms():
    return '\n'.join(
        f"Deluxe room with number {room['room_number']} costs {room['price_per_night']}$ per night!"
        for room
        in HotelRoom.objects
        .filter(room_type='Deluxe')
        .annotate(odd_pk=F("pk") % 2)
        .exclude(odd_pk__gt=0)
        .values("room_number", "price_per_night")
    )


def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')
    prev_reserved_room = None

    for i, room in enumerate(rooms):
        if not room.is_reserved:
            continue

        if prev_reserved_room is not None:
            room.capacity += rooms[prev_reserved_room].capacity
        else:
            room.capacity += room.id
        prev_reserved_room = i

    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room():
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room():
    room = HotelRoom.objects.last()
    if not room.is_reserved:
        room.delete()


# TASK 7

def update_characters():
    def mage(cls):
        if cls.intelligence - 7 >= 0:
            cls.intelligence -= 7
        else:
            cls.intelligence = 0
        cls.level += 3

    def warrior(cls):
        cls.hit_points //= 2
        cls.dexterity += 4

    def ass_scout(cls):
        cls.inventory = "The inventory is empty"

    class_action = {
        "Mage": mage,
        "Warrior": warrior,
        "Assassin": ass_scout,
        "Scout": ass_scout
    }

    characters = Character.objects.all()

    for character in characters:
        class_action.get(character.class_name, lambda x:None)(character)
        character.save()


def fuse_characters(first_character: Character, second_character: Character):

    def fusion_inventories(class_name):
        if class_name in ("Mage","Scout"):
            return "Bow of the Elven Lords, Amulet of Eternal Wisdom"
        return "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=f"{first_character.name} {second_character.name}",
        class_name="Fusion",
        level=floor((first_character.level + second_character.level) // 2),
        strength=floor((first_character.strength + second_character.strength) * 1.2),
        dexterity=floor((first_character.dexterity + second_character.dexterity) * 1.4),
        intelligence=floor((first_character.intelligence + second_character.intelligence) * 1.5),
        hit_points=first_character.hit_points + second_character.hit_points,
        inventory=fusion_inventories(first_character.class_name)
    )
    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()


