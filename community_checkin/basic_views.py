from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# queries: https://www.geeksforgeeks.org/raw-sql-queries-in-django-views/
def index(request):
    template = loader.get_template("")
    return HttpResponse("Hello World")