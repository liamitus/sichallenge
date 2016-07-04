from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)


class Table(models.Model):
    size = models.IntegerField(default=0)
    joinable = models.BooleanField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Reservation(models.Model):
    date = models.DateTimeField('date and time')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)


class Party(models.Model):
    size = models.IntegerField(default=0)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=200)
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)


class Employee(models.Model):
    name = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
