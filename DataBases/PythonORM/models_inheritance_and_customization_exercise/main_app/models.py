from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.


class StudentIDField(models.PositiveIntegerField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_prep_value(self, student_id):
        try:
            student_id = int(student_id)
        except:
            raise ValueError('Invalid input for student ID')
        return student_id

    def clean(self, student_id, obj):
        if int(student_id) <= 0:
            raise ValidationError('ID cannot be less than or equal to zero')
        return student_id


class MaskedCreditCardField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if not isinstance(value,str):
            raise ValidationError("The card number must be a string")
        try:
            int(value)
        except:
            raise ValidationError("The card number must contain only digits")
        if len(str(value)) != 16:
            raise ValidationError("The card number must be exactly 16 characters long")
        return str(value).replace(str(value)[:-4], '****-****-****-')

    def clean(self, value, inst):
        return self.get_prep_value(value)






class BaseCharacter(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100)
    description = models.TextField()


class Mage(BaseCharacter):
    elemental_power = models.CharField(max_length=100)
    spellbook_type = models.CharField(max_length=100)


class Assassin(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    assassination_technique = models.CharField(max_length=100)


class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    demon_slaying_ability = models.CharField(max_length=100)


class TimeMage(Mage):
    time_magic_mastery = models.CharField(max_length=100)
    temporal_shift_ability = models.CharField(max_length=100)


class Necromancer(Mage):
    raise_dead_ability = models.CharField(max_length=100)


class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(max_length=100)
    venomous_bite_ability = models.CharField(max_length=100)


class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(max_length=100)


class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(max_length=100)
    retribution_ability = models.CharField(max_length=100)


class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(max_length=100)


class UserProfile(models.Model):
    username = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)


class Message(models.Model):
    sender = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        self.is_read = True

    def reply_to_message(self, reply_content: str):
        message = Message(sender=self.receiver, receiver=self.sender, content=reply_content)
        message.save()
        return message

    def forward_message(self, receiver: UserProfile):
        message = Message(sender=self.receiver, receiver=receiver, content=self.content)
        message.save()
        return message


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = StudentIDField()


class CreditCard(models.Model):
    card_owner = models.CharField(max_length=100)
    card_number = MaskedCreditCardField()


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class Room(models.Model):
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE)
    number = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField()
    total_guests = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.total_guests > self.capacity:
            raise ValidationError('Total guests are more than the capacity of the room')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args,**kwargs)
        return f'Room {self.number} created successfully'


# @receiver
# def room_saved(post_save, sender=Room):
#     return f"Room {sender.number} created successfully"


class BaseReservation(models.Model):
    class Meta:
        abstract = True

    room = models.ForeignKey(to='Room', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def reservation_period(self):
        return (self.end_date - self.start_date).days

    def calculate_total_cost(self):
        return round((self.room.price_per_night * self.reservation_period()), 2)

    @staticmethod
    def compare_date_ranges(dr1: tuple, dr2: tuple) -> bool:
        for dr in dr1:
            print(dr, *dr2)
            if dr2[0] <= dr <= dr2[1]:
                return True
        return False

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("Start date cannot be after or in the same end date")

        reservations = self.__class__.objects.all()
        for reservation in reservations:
            if BaseReservation.compare_date_ranges((self.start_date, self.end_date),
                                                   (reservation.start_date, reservation.end_date)):
                raise ValidationError(f"Room {self.room.number} cannot be reserved")


class RegularReservation(BaseReservation):
    # a = int('a')
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        return f"Regular reservation for room {self.room.number}"


class SpecialReservation(BaseReservation):

    def extend_reservation(self, days: int):
        self.end_date += timedelta(days=days)
        reservations = self.__class__.objects.filter(
            room=self.room,
            end_date__gte=self.start_date,
            start_date__lte=self.end_date
        )
        if reservations.exists(): raise ValidationError('Error during extending reservation')
        self.save()
        return f"Extended reservation for room {self.room.number} with {days} days"

    def save(self, **kwargs):
        self.clean()
        super().save(**kwargs)
        return f"Special reservation for room {self.room.number}"


# @receiver
# def reservation_saved(post_save, sender=RegularReservation):
#     return f"Regular reservation for room {sender.room.number}"
#
#
# @receiver
# def reservation_saved(post_save, sender=SpecialReservation):
#     return f"Special reservation for room {sender.room.number}"





