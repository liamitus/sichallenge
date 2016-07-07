from django.test import TransactionTestCase
from django.test.client import RequestFactory
from django.utils import timezone

class ReservationTests(TransactionTestCase):
    rf = RequestFactory()

    def test_cannot_make_reservations_in_the_past(self):
        """
        make_reservation() should return an error if a reservation is made for
        a date in the past.
        """

        restaurant = mock_restaurant()
        
        url = '/restaurant/%d/reservation' % restaurant.pk
        mock_request = self.rf.post(url, {
            'date': '%s' % timezone.now(),
            'size': 4
        })

        # make_reservation(mock_request)


    def mock_restaurant(self):
        restaurant = Restaurant(name='Testy\'s Testaurant')
        table = Table(size=4, restaurant = restaurant)

        restaurant.save()
        table.save()

        return restaurant
        
