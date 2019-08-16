from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from core_app.models import CustomUser
from .forms import AgentRegistrationForm
from .models import Agent, VerificicationDocument


class AgentRegistrationView(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = AgentRegistrationForm
    success_message = '%(name)s with %(user.email)s has successfully been registered! Please fill in the profile form.'
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'agent'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        '''Authenticate the user after registering and redirect them
        to AgentProfileCreate'''
        user = form.save()
        login(self.request, user)
        return redirect('registration_success')


class AgentProfileCreateView(LoginRequiredMixin, CreateView):
    model = Agent
    fields = ['name', 'slug', 'is_company', 'is_independent',
            'about', 'phonenumber', 'line_id']
    template_name = 'registration/registration_success.html'
    success_url = reverse_lazy('account:house_list')

    def form_valid(self, form):
        # assign user to requested user
        form.instance.user = self.request.user
        return super().form_valid(form)


class AgentLisView(ListView):
    '''A view that returns all the agents'''
    model = Agent


class AgentSubmitDocumentView(LoginRequiredMixin, CreateView):
    model = VerificicationDocument
    fields = ['name', 'document']
    template_name = 'accounts/document_submit_form.html'
    success_url = reverse_lazy('account:house_list')

    def form_valid(self, form):
        # assign user to requested user
        form.instance.user = self.request.user
        return super().form_valid(form) 


class MyDocumentListView(LoginRequiredMixin, ListView):
    model = VerificicationDocument
    context_object_name = 'document_list'
    template_name = 'accounts/document_list.html'


'''Function views'''

def confirm_verification(request, slug):
    '''Confirm verification by change boolean value to True'''
    agent = Agent.objects.get(slug=slug)
    agent.verified = True
    agent.save()
    # redirect after confirmation
    return redirect('account:document_list')

def verify_agent(request, slug):
    '''View to be called on in uploaded document list to verify an agent''' 
    object = Agent.objects.get(slug=slug)
    context = {
        'object':object,
    }
    return render(request, 'accounts/verify_agent.html', context)
    

    



   