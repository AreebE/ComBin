from django.urls import reverse
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from community_checkin.models import Loan
from community_checkin.query import create_user, get_user, login_user, get_current_loans_of_user

def user_account(request, user_id):
    template = loader.get_template("user/user_form.html")
    context = {"user": get_user(user_id), "loans": get_current_loans_of_user(user_id)}
    return HttpResponse(template.render(context, request))

def produce_account_form(request):
    template = loader.get_template("user/user_account_form.html")
    context = {}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def log_into_account(request):
    user = login_user(name=request.POST["name"], password=request.POST["password"])
    if user != None:
        return HttpResponseRedirect(reverse("community_checkin:user", args=[user.id]))
    else:
        return HttpResponseRedirect("user_form")

@csrf_exempt
def create_account(request):
    user = create_user(name=request.POST["name"], password=request.POST["password"])
    if user != None:
        return HttpResponseRedirect(reverse("community_checkin:user", args=[user.id]))
    else:
        return HttpResponseRedirect("user_form")