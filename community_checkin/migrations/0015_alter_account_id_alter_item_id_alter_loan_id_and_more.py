# Generated by Django 5.1.5 on 2025-05-02 19:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_checkin', '0014_alter_account_id_alter_item_id_alter_loan_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.CharField(default=uuid.UUID('699fc75f-d7e9-4420-996c-bdc682d6f90b'), max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.CharField(default=uuid.UUID('2f642a47-0955-4504-b1ea-720e11421af6'), max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='id',
            field=models.CharField(default=uuid.UUID('07d09e2c-6491-49b0-9e3a-6ad3c8cf6b02'), max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='id',
            field=models.CharField(default=uuid.UUID('687ab077-e393-442e-bf10-5db19ab5cc0c'), max_length=36, primary_key=True, serialize=False, unique=True),
        ),
    ]
