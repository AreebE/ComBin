from django.urls import reverse
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from community_checkin.query import get_item, get_loanable_items, create_loan as create_new_loan, get_user_loan_history, get_loanable_items_with_query
from django.utils import timezone
from datetime import datetime

@csrf_exempt
def item_search(request, user_id):
    template = loader.get_template("user/item/item_search.html")
    loanable_items = get_loanable_items(user_id)
    context={
        "items": loanable_items,
        "user_id": user_id
    }
    return HttpResponse(template.render(context=context, request=request))

@csrf_exempt
def item_search_query(request, user_id):
    template = loader.get_template("user/item/item_search.html")
    loanable_items = get_loanable_items_with_query(user_id, request.POST["query"])
    context={
        "items": loanable_items,
        "user_id": user_id
    }
    return HttpResponse(template.render(context=context, request=request))

@csrf_exempt
def item_history(request, user_id):
    template = loader.get_template("user/item/item_history.html")
    loan_history = get_user_loan_history(user_id)
    context = {
        "loans": loan_history
    }
    return HttpResponse(template.render(context=context, request=request))

def item_loan(request, user_id, item_id):
    template = loader.get_template("user/item/item_loan.html")
    context = {
        "item": get_item(item_id),
        "user_id": user_id
    }
    return HttpResponse(template.render(request=request, context=context))

@csrf_exempt
def create_loan(request, user_id, item_id):
    print(request.POST)
    start_date = datetime.fromisoformat(request.POST["start"])
    end_date = datetime.fromisoformat(request.POST["end"])
    formatted_start = timezone.datetime(year=start_date.year, month=start_date.month, day=start_date.day).date()
    formatted_end = timezone.datetime(year=end_date.year, month=end_date.month, day=end_date.day).date()
    create_new_loan(user_id, item_id,
                    formatted_start, formatted_end)
    return HttpResponseRedirect(reverse("community_checkin:item_search", args=[user_id]))