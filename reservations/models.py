from django.core import serializers
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, time

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500, default='http://i.imgur.com/imPtltl.jpg')

    def get_free_table(self, reservation):
        """
        Receive a table which can accomodate the given reservation,
        or None if no suitable table exists.
        """
        if not reservation:
            return None
        for table in self.table_set.all():
            if table.is_available(reservation) and table.can_seat(reservation):
                return table
        return None


    def get_json(self):
        reservation_array = []
        for t in self.table_set.all():
            for r in t.reservation_set.all():
                reservation_array.append(r.get_json())
        return {
                'id': self.id, 
                'name': self.name,
                'image_url': self.image_url,
                'reservations': list(reservation_array)
                }

    def __str__(self):
        return self.name


class Table(models.Model):
    size = models.IntegerField(default=0)
    joinable = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    EXPECTED_MEAL_TIME_HOURS = 2

    def is_available(self, reservation):
        """
        Check if the table will be available for the given reservation date.
        """
        if not reservation:
            return False

        try:
            same_day_reservations = self.reservation_set.get(date__day=reservation.date.day)
        except Reservation.DoesNotExist:
            same_day_reservations = None
        if same_day_reservations is None:
            return True

        when_table_is_free = same_day_reservations.date + timedelta(hours=self.EXPECTED_MEAL_TIME_HOURS)
        if when_table_is_free < reservation.date:
            return True

        return False

    def can_seat(self, reservation):
        return int(reservation.party.size) <= self.size

    def __str__(self):
        return '%d-person table in %s' % (self.size, self.restaurant)


class Reservation(models.Model):
    date = models.DateTimeField('date and time')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)

    def has_valid_date(self):
        return self.date >= timezone.now()

    def get_json(self):
        return {
                'id': self.id, 
                'date': self.date,
                'size': self.party.size,
                'name': self.party.customer_set.all()[0].name
                }

    def __str__(self):
        s = '%s at %s' % (self.table, self.date)
        if self.table:
            s = '%s for a party of %s' % (s, self.table.size)
        return s


class Party(models.Model):
    size = models.IntegerField(default=0)
    reservation = models.OneToOneField(
            Reservation,
            on_delete=models.CASCADE,
            primary_key=True
    )

    def __str__(self):
        return 'size of %d' % self.size


class Customer(models.Model):
    name = models.CharField(max_length=200)
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)

    def get_existing_reservation(self):
        if not self.party:
            return None
        return self.party.reservation

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
