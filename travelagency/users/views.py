from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import CustomAuthenticationForm, CustomUserCreationForm

class CustomLogoutView(LogoutView):
    def get_next_page(self):
        next_page = super(CustomLogoutView, self).get_next_page()
        messages.add_message(self.request, messages.SUCCESS, 'Success: You successfully log out!')
        return next_page


class CustomLoginView(SuccessMessageMixin, LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'users/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('tours:base_view')


class CustomRegistrationView(View):
    template_name = 'users/registration.html'
    form = CustomUserCreationForm
    message = 'Your account has been created! You are now able to log in.'

    def get(self, request, *args, **kwargs):
        context = {'form':self.form}
        return render(self.request, self.template_name, context)

    def post(self, request, *args,**kwargs):
        form = self.form(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(self.request, messages.SUCCESS, self.message)
            return HttpResponseRedirect('/')

        form = self.form(request.POST)
        context = {'form':form}
        return render(self.request, self.template_name, context)