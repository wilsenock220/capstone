'''
The views here are for the website visitors that are looking for properties.
'''
from .base import *

from ..models import Apartment, ApartmentUnit, House


class ApartmentList(ListView):
    model = Apartment


class ApartmentDetailView(DetailView):
    model = Apartment


class ApartmentUnitDetailView(DetailView):
    model = ApartmentUnit


class HouseListView(ListView):
    # List view for houses that are available
    queryset = House.objects.filter(available=True)


class HouseDetailView(DetailView):
    model = House



