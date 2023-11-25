from unittest import TestCase
from project.trip import Trip


class TestTrip(TestCase):

    def setUp(self):
        self.group = Trip(
            10000,
            10,
            False
        )
        self.family = Trip(
            2000,
            4,
            True
        )

    def test_initialization(self):
        group,family = self.group, self.family
        self.assertEqual(group.budget, 10000)
        self.assertEqual(group.travelers, 10)
        self.assertEqual(group.is_family, False)
        self.assertEqual(group.booked_destinations_paid_amounts, {})
        self.assertEqual(family.is_family, True)
        self.assertEqual(group.DESTINATION_PRICES_PER_PERSON,family.DESTINATION_PRICES_PER_PERSON)

    def test_travelers_set(self):
        group = self.group
        group.travelers += 1
        self.assertEqual(group._travelers, 11)
        with self.assertRaises(ValueError) as ve:
            group.travelers = 0
        self.assertEqual(str(ve.exception), 'At least one traveler is required!')

    def test_is_family_set(self):
        family,group = self.family, self.group
        self.assertTrue(family._is_family)
        self.assertFalse(group._is_family)
        family.travelers = 1
        family.is_family = True
        self.assertFalse(family.is_family)
        family.travelers = 2
        self.assertFalse(family.is_family)
        family.is_family = True
        self.assertTrue(family.is_family)

    def test_book_a_trip(self):
        group,family = self.group,self.family
        self.assertEqual(group.book_a_trip("Old Zealand"),'This destination is not in our offers, please choose a new one!')
        self.assertEqual(family.book_a_trip("New Zealand"), 'Your budget is not enough!')
        self.assertEqual(family.book_a_trip("Bulgaria"), f'Successfully booked destination Bulgaria! Your budget left is {200:.2f}')
        self.assertEqual(group.book_a_trip("Bulgaria"), f'Successfully booked destination Bulgaria! Your budget left is {5000:.2f}')
        self.assertEqual(family.booked_destinations_paid_amounts,{"Bulgaria":1800})


    def test_booking_status(self):
        family,group = self.family,self.group
        self.assertEqual(family.booking_status(), f'No bookings yet. Budget: {family.budget:.2f}')
        family.book_a_trip("Bulgaria")
        self.assertEqual(
            family.booking_status(),
            """Booked Destination: Bulgaria
Paid Amount: 1800.00
Number of Travelers: 4
Budget Left: 200.00"""
        )
