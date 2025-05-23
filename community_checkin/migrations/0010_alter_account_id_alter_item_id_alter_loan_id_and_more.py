# Generated by Django 5.1.5 on 2025-05-02 18:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_checkin', '0009_alter_account_id_alter_item_id_alter_loan_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bf01cd9b-8fcf-4fe3-9d0e-0a1a850e305a'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.UUIDField(default=uuid.UUID('836d4c82-dbdd-426a-a39f-10c17aa6b40e'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e71788c8-2335-4717-819b-7d3a971a4662'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='id',
            field=models.UUIDField(default=uuid.UUID('51cc17a3-b74e-4b1a-b609-c6ae0712f492'), primary_key=True, serialize=False, unique=True),
        ),
    ]
