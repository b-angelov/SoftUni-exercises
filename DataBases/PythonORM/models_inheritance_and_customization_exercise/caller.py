import os
from datetime import date

import django
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Mage, Necromancer, UserProfile, Message, Student, CreditCard, SpecialReservation, Room, \
    Hotel, RegularReservation

# Create queries within functions

# Create instances


if __name__ == '__main__':
    Hotel.objects.all().delete()
    Room.objects.all().delete()
    SpecialReservation.objects.all().delete()
    RegularReservation.objects.all().delete()
    # Create a Hotel instance
    hotel = Hotel.objects.create(name="Hotel ABC", address="123 Main St")

    # Create Room instances associated with the hotel
    room1 = Room.objects.create(
        hotel=hotel,
        number="102",
        capacity=2,
        total_guests=1,
        price_per_night=100.00
    )

    # Create SpecialReservation instance
    special_reservation1 = SpecialReservation(
        room=room1,
        start_date=date(2023, 1, 1),
        end_date=date(2023, 1, 5)
    )

    # Create a special reservation1
    print(special_reservation1.save())

    # Create SpecialReservation instance
    special_reservation2 = RegularReservation(
        room=room1,
        start_date=date(2023, 1, 10),
        end_date=date(2023, 1, 12)
    )

    # Create a special reservation2
    print(special_reservation2.save())

    # Calculate total cost for special reservation1
    print(special_reservation1.calculate_total_cost())

    # Calculate reservation period for special reservation1
    print(special_reservation1.reservation_period())

    # Example of extending a SpecialReservation
    try:
        print(special_reservation1.extend_reservation(5))
    except ValidationError as e:
        print(e)




