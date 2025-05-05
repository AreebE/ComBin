from django.urls import reverse
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from community_checkin.query import get_manager, create_item, update_item as update_item_sql, get_item, delete_item as delete_item_sql, get_item_loan_history
from community_checkin.models import Item

def item_view(request, manager_id, item_id):
    template = loader.get_template("manager/item/item_edit_form.html")
    context = {
        "item": get_item(item_id),
        "manager_id": manager_id,
        "loans": get_item_loan_history(item_id)
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def add_item(request, manager_id):
    name = request.POST["name"]
    loan_count = request.POST["loan_count"]
    content = request.POST["content"]
    create_item(name, loan_count, content, get_manager(manager_id))
    return HttpResponseRedirect(reverse("community_checkin:manager", args=[manager_id]))
    # return HttpResponse("Sample");

@csrf_exempt
def update_item(request, manager_id, item_id):
    name = request.POST["name"]
    loan_count = request.POST["loan_count"]
    content = request.POST["content"]
    item = get_item(item_id)
    update_item_sql(item, "name", name)
    update_item_sql(item, "loan_count", loan_count)
    update_item_sql(item, "content", content)
    return HttpResponseRedirect(reverse("community_checkin:manager", args=[manager_id]))

@csrf_exempt
def delete_item(request, manager_id, item_id):
    item = get_item(item_id)
    delete_item_sql(item)
    return HttpResponseRedirect(reverse("community_checkin:manager", args=[manager_id]))