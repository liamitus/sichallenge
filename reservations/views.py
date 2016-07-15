import json

from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import *
from django.utils.dateparse import parse_datetime

from reservations.models import *

def index(request):
    return redirect('/static/index.html')
    # return render_to_response('sichallenge/index.html')


def get_all_restaurants(request):
    all_restaurants = [r.get_json() for r in Restaurant.objects.all()]
    return JsonResponse(dict(restaurants=all_restaurants))


def make_reservation(request, restaurant_id):
    """
    Make a reservation at the given restaurant.
    Request body must be a JSON object that contains the following properties:
        - date
        - name
        - size
    """
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    # TODO clean up this method
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        customer = get_or_create_customer(body['name'])
        existing_reservation = customer.get_existing_reservation()
        if existing_reservation is not None:
            return error_response('existing reservation')
        reservation_obj = Reservation(date=parse_datetime(body['date']))
        reservation_obj.save()
        party = Party(size=body['size'], reservation=reservation_obj)
        party.save()
        customer.party = party
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


def get_or_create_customer(customer_name):
    try:
        customer = Customer.objects.get(name=customer_name)
    except Customer.DoesNotExist:
        customer = Customer(name=customer_name)
    return customer


def error_response(msg):
    response = JsonResponse({'error': str(msg)})
    response.status_code = 400
    return response
