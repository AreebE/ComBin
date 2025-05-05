from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request)) 