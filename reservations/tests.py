from django.test import TransactionTestCase
from django.test import Client
from django.utils import timezone

from datetime import timedelta

from reservations.models import *

class ReservationTests(TransactionTestCase):

    def test_cannot_make_reservations_in_the_past(self):
        """
        make_reservation() should return an error if a reservation is made for
        a date in the past.
        """
        client = Client()

        restaurant = self.mock_restaurant()
        customer = self.mock_customer()

        url = '/restaurant/%d/reservation' % restaurant.pk
        response = client.post(url, {
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


    def mock_customer(self):
        customer = Customer(name='Testy Tester')
        customer.save()

        return customer


    def mock_restaurant(self):
        r = Restaurant(name='Testy\'s Testaurant')
        r.save()

        table = Table(size=4, restaurant=r)
        table.save()

        return r
        
