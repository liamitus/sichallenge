from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500, default='http://i.imgur.com/imPtltl.jpg')

    def get_free_table(self, reservation):
        for table in self.table_set.all():
            if table.is_available(reservation):
                return table
        return None

    def __str__(self):
        return self.name


class Table(models.Model):
    size = models.IntegerField(default=0)
    joinable = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def is_available(self, reservation):
        expected_meal_time_hours = 2
        same_day_reservations = self.reservation_set.get(date__day=reservation.day)
        if not same_day_reservations:
            return True
        for existing_reservation in same_day_reservations:
            when_table_is_free = existing_reservation.date + timedelta(hours=expected_meal_time_hours)
            if when_table_is_free < reservation.date and reservation.party.size <= self.size:
                return True
        return False

    def __str__(self):
        return 'size of %d in %s' % (self.size, self.restaurant)


class Reservation(models.Model):
    date = models.DateTimeField('date and time')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)

    def has_valid_date(self):
        return self.date >= timezone.now()

    def __str__(self):
        s = '%s at %s for a party of %s' 
        return s % (self.table, self.date, self.table.size)


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

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
