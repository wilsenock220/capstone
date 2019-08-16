'''
This module contains all the views for the agent.
The views allows the agent to do CRUD operations on the aparmentunit object
'''
from .base import *

from ..models import Apartment, ApartmentUnit, House 


class MyApartmentListView(ListView):
    '''A list view for website visitors'''
    model = Apartment
    template_name = 'properties/my_apartment_list.html'


class ApartmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    '''Create Apartment view for content managers'''
    model = Apartment
    fields = ['name', 'slug', 'description', 'floors', 'shopping_mall',
        'gym', 'swimming_pool', 'jogging_track', 'laundry', 'security', 'image']
    success_message = 'Apartment %(name)s successfully added'


class ApartmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    '''Update apartment for content managers'''
    model = Apartment
    fields = ['name', 'slug', 'description', 'floors', 'shopping_mall',
        'gym', 'swimming_pool', 'jogging_track', 'laundry', 'security', 'image']
    success_message = '%(name)s has been successfully updated'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ApartmentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Apartment
    success_url = reverse_lazy('account:apartment_list')
    success_message = 'Apartment has been deleted'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ApartmentDeleteView, self).delete(request, *args, **kwargs)


class ApartmentUnitListView(ListView):
    model = ApartmentUnit


class MyApartmentUnitListView(LoginRequiredMixin, ListView):
    model = ApartmentUnit
    template_name = 'properties/my_apartment_unit.html'

    def get_queryset(self):
        return ApartmentUnit.objects.filter(owner=self.request.user)


class ApartmentUnitCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ApartmentUnit
    fields = ['apartment', 'title', 'slug', 'deposit', 'rent_per_month', 'description',
        'furnishing', 'bedrooms', 'size', 'water_heating', 'available', 
        'floor', 'balcony','image']
    success_message = 'Unit "%(title)s" successfully added'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ApartmentUnitUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ApartmentUnit
    fields = ['apartment', 'title', 'slug', 'deposit', 'rent_per_month', 'description',
        'furnishing', 'bedrooms', 'size', 'water_heating', 'available', 
        'floor', 'balcony','image', 'available']
    success_message = '%(title)s successfully updated'
    template_name = 'properties/apartmentunit_update.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ApartmentUnitDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ApartmentUnit
    success_url = reverse_lazy('account:apartmentunit_list')
    success_message = '%(title)s has been deleted'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ApartmentUnitDeleteView, self).delete(request, *args, **kwargs)


    
