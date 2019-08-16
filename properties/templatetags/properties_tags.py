from django import template
from django.template import RequestContext
from ..models import ApartmentUnit,  Apartment, House

register = template.Library()

@register.simple_tag
def apartmentunit_list():
    unit_list = ApartmentUnit.objects.all()
    return unit_list[0:3]


@register.simple_tag
def house_list():
    house_list = House.objects.all()
    return house_list[0:3]

