from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

def index(request):
    return HttpResponse("Find a table nearby.")

def make_reservation(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, restaurant_id)
    try:
        reservation_obj = Reservation(date=request.POST['date'])
        party = Party(size=request.POST['size'], reservation=reservation_obj)
        customer = get_or_create_customer(request, party)
    except Exception as e:
        return errorResponse(e)
    
    table = restaurant.get_free_table(reservation_obj)
    if not table:
        return errorResponse('no free tables for that time')

    reservation_obj.table = table
    customer.party = party

    reservation_obj.save()
    party.save()
    customer.save()
    return JsonResponse()


def get_or_create_customer(resquest, party):
    try:
        customer = Customer.objects.get(name=request.POST['name'])
    except Customer.DoesNotExist:
        customer = Customer(name=request.POST['name'])
    customer.party = party
    return customer


def errorResponse(msg):
    return JsonResponse({'error': msg})
