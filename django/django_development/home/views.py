"""
views for home page
"""
from django.views.generic import TemplateView


# Create your views here.

class HomeView(TemplateView):
    """TODO"""
    template_name = 'home.html'

