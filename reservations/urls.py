from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/reservation$', views.make_reservation, name='make_reservation')
]
