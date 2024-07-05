from datetime import date

from django.test import TestCase

from caller import register_car_by_owner
from main_app.models import Owner, Car, Registration


class CarRegistrationTestClass(TestCase):
    def setUp(self):
        """
        Note: Test data for zero tests!
        """
        self.owner1 = Owner.objects.create(name='Ivelin Milchev')
        self.owner2 = Owner.objects.create(name='Alice Smith')
        self.car1 = Car.objects.create(model='Citroen C5', year=2004)
        self.car2 = Car.objects.create(model='Honda Civic', year=2021)
        self.registration1 = Registration.objects.create(registration_number='TX0044XA')
        self.registration2 = Registration.objects.create(registration_number='XYZ789')

    def test_zero_car_registration(self):
        """
        Zero test case: Register a car by owner
        """
        result = register_car_by_owner(self.owner1)
        expected_result = 'Successfully registered Citroen C5 to Ivelin Milchev with registration number TX0044XA.'
        self.assertEqual(result, expected_result)

        self.car1.refresh_from_db()
        self.assertEqual(self.car1.owner, self.owner1)
        self.assertEqual(self.car1.registration, self.registration1)
        self.assertEqual(self.car1.registration.registration_date, date.today())
