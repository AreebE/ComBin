from django.urls import path
from community_checkin.views import manager_form_view, manager_item_view
from community_checkin.views import user_form_view, user_item_view
from community_checkin.views import index
app_name="community_checkin"
urlpatterns = [
    # Logging in
    path("", index.index, name="index"),
    
    # - user
    path("user_form", user_form_view.produce_account_form, name="user_form"),
    path("login_user", user_form_view.log_into_account, name="login_user"),
    path("create_user", user_form_view.create_account, name="create_user"),
    # - manager
    path("manager_form", manager_form_view.produce_account_form, name="manager_form"),
    path("login_manager", manager_form_view.log_into_account, name="login_manager"),
    path("create_manager", manager_form_view.create_account, name="create_manager"),
    
    # Manager stuff
    # - item view
    path("<str:manager_id>/manager", manager_form_view.manager_account, name="manager"),
    path("<str:manager_id>/add_item", manager_item_view.add_item, name="add_item"),
    path("<str:manager_id>/<str:item_id>/item", manager_item_view.item_view, name="item"),
    path("<str:manager_id>/<str:item_id>/update_item", manager_item_view.update_item, name="update_item"),
    path("<str:manager_id>/<str:item_id>/delete_item", manager_item_view.delete_item, name="delete_item"),
    
    # User stuff
    path("<str:user_id>/user", user_form_view.user_account, name="user"),
    # Loaning
    path("<str:user_id>/user/item_search", user_item_view.item_search, name="item_search"),
    path("<str:user_id>/user/item_search_q", user_item_view.item_search_query, name="item_search_query"),
    path("<str:user_id>/user/item_history", user_item_view.item_history, name="item_history"),
    path("<str:user_id>/user/item_search/<str:item_id>/item_loan", user_item_view.item_loan, name="item_loan"),
    path("<str:user_id>/user/item_search/<str:item_id>/create_loan", user_item_view.create_loan, name="create_loan")
]