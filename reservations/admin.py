from django.contrib import admin

from .models import Customer, Employee, Party, Reservation, Restaurant, Table

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Party)
admin.site.register(Reservation)
admin.site.register(Restaurant)
admin.site.register(Table)
