'''
This module contains the views for the agent.
eg. Creating, Retreiving, Updating and deleting their objects.
'''
from .base import *
from ..models import House


class MyHouseListView(LoginRequiredMixin, ListView):
    '''Personal list of object for the authenticated agent'''
    model = House
    template_name = 'properties/agent_house_list.html'

    def get_queryset(self):
        # only show agent owned property
        return House.objects.filter(owner=self.request.user)


# view should only be accessable for property agents
class HouseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = House
    fields = ['title', 'slug', 'deposit', 'rent_per_month', 'description',
        'furnishing', 'bedrooms', 'bathrooms', 'floors', 'size', 'water_heating', 'image']
    template_name = 'properties/house_create_form.html'
    success_message = '%(title)s successfully added'

    def form_valid(self, form):
        # assign owner field to logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class HouseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = House
    fields = ['title', 'slug', 'deposit', 'rent_per_month', 'description',
        'furnishing', 'bedrooms', 'bathrooms', 'floors', 'size', 'water_heating', 'available', 'image']
    template_name = 'properties/house_update_form.html'
    success_message = '%(title)s has been updated successfully'

    def form_valid(self, form):
        # assign owner field to logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class HouseDeleteView(LoginRequiredMixin, DeleteView):
    model = House
    success_url = reverse_lazy('account:house_list')
    success_message = 'Successfully deleted'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(HouseDeleteView, self).delete(request, *args, **kwargs)