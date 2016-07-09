from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_datetime

from reservations.models import *

def index(request):
    return HttpResponse("Find a table nearby.")

def make_reservation(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    try:
        reservation_obj = Reservation(date=parse_datetime(request.POST['date']))
        party = Party(size=request.POST['size'], reservation=reservation_obj)
        customer = get_or_create_customer(request.POST['name'], party)
    except Exception as e:
        return error_response(e)

    if not reservation_obj.has_valid_date():
        return error_response('invalid date')
    
    table = restaurant.get_free_table(reservation_obj)
    if not table:
        return error_response('no free tables for that time')

    reservation_obj.table = table
    customer.party = party

    reservation_obj.save()
    party.save()
    customer.save()

    return JsonResponse()


def get_or_create_customer(customer_name, party):
    try:
        customer = Customer.objects.get(name=customer_name)
    except Customer.DoesNotExist:
        customer = Customer(name=customer_name)
    customer.party = party
    return customer


def error_response(msg):
    response = JsonResponse({'error': str(msg)})
    response.status_code = 400
    return response
