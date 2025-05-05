from community_checkin.models import *
from django.utils import timezone
from django_prepared_query import BindParam
from datetime import datetime
from pytz import UTC
from uuid import uuid4

# 6 = object
# 8 = Prepared
# 11 = either
# Sum is 25. 20% of 25 is 5, so both object and
# prepared statements meet this requirement, regardless of what
# the 'either' statements would be classified as. (They most likely
# count as object, but I thought it would be safe to consider the worst
# case scenario since you do substitute in parameters like in prepared
# statements.)

# Manager

def create_manager(name, password):
    query = Manager.objects.raw("SELECT * FROM community_checkin_manager WHERE name = %s",
                                params = [name]) # Prepared
    if (len(query) == 0):
        new_id = uuid4()
        # Either
        while (len(Manager.objects.filter(id=new_id)) != 0):
            new_id = uuid4()
        manager = Manager(id=new_id, name=name, password=password)
        manager.save() # Object
        return manager
    return None

def login_manager(name, password):
    query = Manager.objects.raw("SELECT * FROM community_checkin_manager WHERE name = %s AND password = %s",
                                params = [name, password]) # Prepared
    if (len(query) == 1):
        return query[0]
    return None
        
def get_manager(manager_id):
    query = Manager.objects.raw("SELECT * FROM community_checkin_manager WHERE id = %s",
                                params = [manager_id]) # Prepared
    return query[0]

# User 

def login_user(name, password):
    query = Account.objects.raw("SELECT * FROM community_checkin_account WHERE name = %s AND password = %s",
                                params = [name, password]) # Prepared
    if (len(query) == 1):
        return query[0]
    return None

def get_user(user_id):
    query = Account.objects.raw("SELECT * FROM community_checkin_account WHERE id = %s",
                                params = [user_id]) # Prepared
    return query[0]

def create_user(name, password):
    query = Account.objects.raw("SELECT * FROM community_checkin_account WHERE name = %s",
                                params = [name]) # Prepared
    if (len(query) == 0):
        new_id = uuid4()
        # Either
        while (len(Account.objects.filter(id=new_id)) != 0):
            new_id = uuid4()
        user = Account(id=new_id, name=name, password=password)
        user.save() # Object
        return user
    return None

# Items
def get_item(item_id):
    query = Item.objects.filter(id=item_id) # Either
    return query[0]

def create_item(name, loan_count, content, manager_id):
    new_id = uuid4()
    # Either
    while (len(Item.objects.filter(id=new_id)) != 0):
        new_id = uuid4()
    item = Item(id=new_id, name=name, loan_count=loan_count, content=content, owner=manager_id)
    item.save() # Object
    return item

def update_item(item, attribute, new_att):
    match attribute:
        case 'name':
            item.name = new_att
        case 'loan_count':
            item.loan_count = new_att
        case 'content':
            item.content = new_att
    item.save() # Object

def delete_item(item):
    item.delete() # Object

def get_items(manager_id):
    query = Item.objects.raw("SELECT * FROM community_checkin_item WHERE owner_id = %s",
                            params = [manager_id]) # Prepared
    return query

# Loans
def create_loan(user_id, item_id, start_date, end_date):
    new_id = uuid4()
    # Either
    while (len(Loan.objects.filter(id=new_id)) != 0):
        new_id = uuid4()
    loan = Loan(id=new_id, loanee=get_user(user_id), item=get_item(item_id), start_date=start_date, end_date=end_date)
    loan.save() # Object
    return loan

def get_user_loan_history(user_id):
    # Either
    loans = Loan.objects.filter(loanee=user_id)
    user_loans = []
    for loan in loans:
        user_loans.append({
                "owner":loan.item.owner.name,
                "item_name":loan.item.name,
                "content":loan.item.content,
                "start_date":loan.start_date,
                "end_date":loan.end_date})
    return user_loans

def get_current_loans_of_user(user_id):
    # for loan in Loan.objects.all():
    #     loan.delete()
    
    today = UTC.localize(datetime.now())
    # Either
    loans = Loan.objects.filter(loanee=user_id)
    user_loans = []
    for loan in loans:
        localized_start = UTC.localize(datetime.fromisoformat(loan.start_date.isoformat()))
        localized_end = UTC.localize(datetime.fromisoformat(loan.end_date.isoformat()))
        if (localized_start < today
                and localized_end > today):
            user_loans.append({
                    "owner":loan.item.owner.name,
                    "item_name":loan.item.name,
                    "content":loan.item.content,
                    "start_date":loan.start_date,
                    "end_date":loan.end_date})
    return user_loans

def get_loanable_items(user_id):
    today = UTC.localize(datetime.now())
    # Either
    currently_loaned_objects = Loan.objects.filter(loanee=user_id)
    excluded_item_ids = set()
    for loan in currently_loaned_objects:
        localized_start = UTC.localize(datetime.fromisoformat(loan.start_date.isoformat()))
        localized_end = UTC.localize(datetime.fromisoformat(loan.end_date.isoformat()))
        if (localized_start < today
                and localized_end > today):
            excluded_item_ids.add(loan.item.id)
    # Either
    items = Item.objects.all()
    loanable_items = []
    for item in items:
        if item.id not in excluded_item_ids:
            loanable_items.append({
                "owner":item.owner.name,
                "item_id":item.id,
                "item_name":item.name,
                "content":item.content,
                "loan_count":item.loan_count
            })
    return loanable_items
    
def get_loanable_items_with_query(user_id, query_str):
    today = UTC.localize(datetime.now())
    # Either
    currently_loaned_objects = Loan.objects.filter(loanee=user_id)
    excluded_item_ids = set()
    for loan in currently_loaned_objects:
        localized_start = UTC.localize(datetime.fromisoformat(loan.start_date.isoformat()))
        localized_end = UTC.localize(datetime.fromisoformat(loan.end_date.isoformat()))
        if (localized_start < today
                and localized_end > today):
            excluded_item_ids.add(loan.item.id)
    # Prepared
    items = Item.objects.raw("SELECT * FROM community_checkin_item item WHERE " \
        + "(item.name LIKE %s) OR (item.content LIKE %s)", 
        params=["%" + query_str + "%", "%" + query_str + "%"])
    loanable_items = []
    for item in items:
        if item.id not in excluded_item_ids:
            loanable_items.append({
                "owner":item.owner.name,
                "item_id":item.id,
                "item_name":item.name,
                "content":item.content,
                "loan_count":item.loan_count
            })
    return loanable_items
    

def get_item_loan_history(item_id):
    # Either
    relevant_loans = Loan.objects.filter(item=item_id)
    items = []
    for loan in relevant_loans:
        items.append({
            "loanee":loan.loanee.name,
            "start_date":loan.start_date,
            "end_date":loan.end_date
        })
    return items
