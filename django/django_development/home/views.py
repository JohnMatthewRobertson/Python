"""
views for home page
"""
from django.http import HttpResponse


# Create your views here.

def home_page_view(request):
    """returns HttResponse hello world"""
    return HttpResponse('Hello World')
