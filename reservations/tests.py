from django.test import TransactionTestCase
from django.test import Client
from django.utils import timezone
from django.core.urlresolvers import reverse

from datetime import timedelta

from reservations.models import *

class ReservationTests(TransactionTestCase):

    client = Client()

    def test_get_all_restaurants(self):
        """
        get_all_restaurants() should return an array containing all restaurants.
        """
        restaurants = self.mock_restaurant_array()

        response = self.client.get(reverse('get_all_restaurants'))

        self.assertEqual(response.status_code, 200)


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

        # all_reservations = set(Reservation.objects.all())
        # while all_reservations:
            # r = all_reservations.pop()
            # customers = r.party.customer_set()
            # while customers:
                # c = customers.pop()
                # self.assertEqual(c, customer)


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
        
