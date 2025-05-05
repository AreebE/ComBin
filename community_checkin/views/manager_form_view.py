from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from community_checkin.query import get_manager, get_items, login_manager, create_item, update_item, delete_item, create_manager
import os
from community_checkin.models import Manager

def manager_account(request, manager_id):
    manager = get_manager(manager_id=manager_id)
    items = get_items(manager_id)
    template = loader.get_template("manager/manager_form.html")
    context = {
        "manager": manager,
        "items": items
    }
    return HttpResponse(template.render(context, request))

def produce_account_form(request):
    template = loader.get_template("manager/manager_account_form.html")
    context = {}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def log_into_account(request): 
    manager = login_manager(name=request.POST["name_l"], password=request.POST["password_l"])
    if manager != None:
        return HttpResponseRedirect(reverse("community_checkin:manager", args=[manager.id]))
    else:
        return HttpResponseRedirect("manager_form")

@csrf_exempt
def create_account(request):
    manager = create_manager(name=request.POST["name_c"], password=request.POST["password_c"])
    if manager != None:
        return HttpResponseRedirect(reverse("community_checkin:manager", args=[manager.id]))
    else:
        return HttpResponseRedirect("manager_form")

