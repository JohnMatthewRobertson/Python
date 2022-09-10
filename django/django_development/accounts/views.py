"""TODO"""
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import CustomUserCreationForm


# Create your views here.

class SignupView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'