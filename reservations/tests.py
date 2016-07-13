import json

from django.test import *
from django.utils import timezone
from django.core.urlresolvers import reverse

from datetime import timedelta

from reservations.models import *

class ReservationTests(TransactionTestCase):

    client = Client()

    # Models - Restaurant

    def test_restaurant_get_free_table_no_tables(self):
        """
        get_free_table() should return None when no suitable table exists.
        """
        restaurant = Restaurant(name="Testy's Tableless Testaurant")
        reservation = Reservation(date=timezone.now())
        self.assertEqual(restaurant.get_free_table(reservation), None)


    def test_restaurant_get_free_table_no_reservation(self):
        """
        get_free_table() should return None when passed no reservation.
        """
        restaurant = self.mock_restaurant()
        self.assertEqual(restaurant.get_free_table(None), None)


    # Models - Table

    def test_table_is_available_after_previous_reservation(self):
        """
        is_available() should return True if the given reservation is for a
        date later than the previous reservation plus the expected meal time.
        """
        restaurant = self.mock_restaurant()
        table = restaurant.table_set.all()[0]
        now = timezone.now()
        first_reservation = self.mock_reservation(date=now, table=table)
        after_first_reservation = now + timedelta(hours=table.EXPECTED_MEAL_TIME_HOURS, seconds=1)
        second_reservation = Reservation(date=after_first_reservation)
        self.assertEqual(table.is_available(second_reservation), True)


    def test_table_is_not_available_one_minute_before_previous(self):
        """
        is_available() should return False if the given reservation is for a
        date equal to the previous reservation minus one minute less than the
        expected meal time.
        """
        restaurant = self.mock_restaurant()
        table = restaurant.table_set.all()[0]
        now = timezone.now()
        first_reservation = self.mock_reservation(date=now, table=table)
        after_first_reservation = now + timedelta(hours=table.EXPECTED_MEAL_TIME_HOURS)
        almost_after_first_reservation = after_first_reservation - timedelta(minutes=1)
        second_reservation = Reservation(date=after_first_reservation)
        self.assertEqual(table.is_available(second_reservation), False)


    def test_table_is_available_no_reservation(self):
        """
        is_available() should return False when passed no reservation.
        """
        table = Table()
        self.assertEqual(table.is_available(None), False)


    def test_table_cannot_seat_party_too_large(self):
        """
        can_seat() should return False when the party of the given reservation
        is too large.
        """
        table = Table(size=2)
        reservation = self.mock_reservation(size=3)
        self.assertEqual(table.can_seat(reservation), False)


    def test_table_can_seat_party_same_size_as_table(self):
        """
        can_seat() should return True when the party of the given reservation
        is exactly the size of the table.
        """
        table = Table(size=2)
        reservation = self.mock_reservation(size=2)
        self.assertEqual(table.can_seat(reservation), True)


    # Views

    def test_get_all_restaurants(self):
        """
        get_all_restaurants() should return an array containing all restaurants.
        """
        restaurants = self.mock_restaurant_array()
        response = self.client.get(reverse('get_all_restaurants'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.contains_restaurants(response, restaurants), True)


    def test_cannot_make_reservations_in_the_past(self):
        """
        make_reservation() should return an error if a reservation is made for
        a date in the past.
        """
        restaurant = self.mock_restaurant()
        customer = self.mock_customer()
        url = '/restaurant/%d/reservation' % restaurant.pk
        response = self.client.post(url, {
            'date': timezone.now() - timedelta(days=1),
            'size': 4,
            'name': customer.name
        })
        self.assertEqual(response.status_code, 400)


    def test_cannot_make_multiple_reservations(self):
        """
        make_reservation() should return an error if a reservation is made for
        a customer that already has a reservation.
        """
        restaurant = self.mock_restaurant()
        customer = self.mock_customer()
        url = '/restaurant/%d/reservation' % restaurant.pk
        response = self.client.post(url, json.dumps({
            'date': str(timezone.now() + timedelta(days=1)),
            'size': 4,
            'name': customer.name
        }), content_type='text/json')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(url, {
            'date': timezone.now() + timedelta(days=2),
            'size': 4,
            'name': customer.name
        }, content_type='text/json')
        self.assertEqual(response.status_code, 400)


    # Helpers

    def contains_restaurants(self, response, restaurants):
        """
        contains_restaurants() checks if the given response contains all of
        the given restaurants by name.
        """
        json_string = response.content
        data = json.loads(str(json_string, 'utf8'))
        for r in restaurants:
            if not any(d['name'] == r.name for d in data['restaurants']):
                return False
        return True

    
    # Mock helpers

    def mock_customer(self, name='Testy Tester'):
        customer = Customer(name=name)
        customer.save()

        return customer

    
    def mock_restaurant_array(self, num_restaurants_to_mock=3):
        mock_restaurants = []
        for n in range(0, num_restaurants_to_mock):
            mock_restaurants.append(self.mock_restaurant('Testy\'s Testaurant %s' % n))
        return mock_restaurants
        

    def mock_restaurant(self, name='Testy\'s Testaurant'):
        r = Restaurant(name=name)
        r.save()

        table = Table(size=4, restaurant=r)
        table.save()

        return r
        

    def mock_reservation(self, table=None, date=timezone.now(), size=1):
        reservation = Reservation(date=date, table=table)
        reservation.save()
        party = Party(size=size)
        party.save()
        reservation.party = party
        return reservation
