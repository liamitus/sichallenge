import json
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_datetime

from reservations.models import *

def index(request):
    return HttpResponse("Find a table nearby.")


def get_all_restaurants(request):
   all_restaurants = [r.get_json() for r in Restaurant.objects.all()]
   return JsonResponse(dict(restaurants=all_restaurants))


def make_reservation(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        reservation_obj = Reservation(date=parse_datetime(body['date']))
        reservation_obj.save()
        party = Party(size=body['size'], reservation=reservation_obj)
        party.save()
        customer = get_or_create_customer(body['name'], party)
    except Exception as e:
        return error_response(e)

    if not reservation_obj.has_valid_date():
        return error_response('invalid date')
    
    table = restaurant.get_free_table(reservation_obj)
    if not table:
        return error_response('no free tables for that time')

    reservation_obj.table = table
    reservation_obj.save()

    customer.party = party
    customer.save()

    return JsonResponse({'success': 'true'})


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
