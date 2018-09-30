from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from contacts.forms import FeedbackForm,FormRegistration,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.

class Feedback(CreateView):
    template_name = 'contacts/feedback.html'
    form_class = FeedbackForm
    success_url = '/feedback'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,'Обратная связь отправлена!')
        return response


class Contacts(TemplateView):
    template_name = 'contacts/contact.html'


class Registration(CreateView):
    template_name = 'registration/registration.html'
    form_class = FormRegistration
    success_url = '/'

