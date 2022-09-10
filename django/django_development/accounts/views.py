"""TODO"""
from accounts.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

class SignupView(generic.CreateView):
    """TODO"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
