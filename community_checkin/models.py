from django.db import models
from uuid import uuid4
# https://www.w3schools.com/django/django_update_data.php 

# Create your models here.
class Account(models.Model):
    id = models.CharField(max_length=36, primary_key=True, unique=True, default=uuid4(), db_index=False)
    name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    class Meta:
        indexes = [
            models.Index(fields=["id"], name="account_id_ind"),
            models.Index(fields=["name", "password"], name="account_login_ind")
        ]

class Item(models.Model):
    id = models.CharField(max_length=36, primary_key=True, unique=True, default=uuid4(), db_index=False)
    name = models.CharField(max_length=30)
    loan_count = models.IntegerField()
    content = models.CharField(max_length=300)
    owner = models.ForeignKey("Manager", on_delete=models.CASCADE)
    class Meta:
        indexes = [
            models.Index(fields=["id"], name="item_id_ind"),
            models.Index(fields=["owner"], name="item_owner_ind")
        ]

class Manager(models.Model):
    id = models.CharField(max_length=36, primary_key=True, unique=True, default=uuid4(), db_index=False)
    name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    class Meta:
        indexes = [
            models.Index(fields=["name", "password"], name="manager_login_ind")
        ]

class Loan(models.Model):
    id = models.CharField(max_length=36, primary_key=True, unique=True, default=uuid4(), db_index=False)
    loanee = models.ForeignKey("Account", on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    class Meta:
        indexes = [
            models.Index(fields=["loanee"], name="loan_loanee_ind"),
            models.Index(fields=["start_date", "end_date"], name="loan_sdate_ind")
        ]
