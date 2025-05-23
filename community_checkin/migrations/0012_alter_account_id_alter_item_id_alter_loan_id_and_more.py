# Generated by Django 5.1.5 on 2025-05-02 18:30

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_checkin', '0011_alter_account_id_alter_item_id_alter_loan_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.UUIDField(default=uuid.UUID('577d5b4e-915e-4f2b-a856-955aa224b27a'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6715f00f-c1ec-483a-915f-fa68d624ae4a'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='id',
            field=models.UUIDField(default=uuid.UUID('16a3a02e-a54c-410f-b9f5-3744012a617d'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='item',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='community_checkin.item'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loanee',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='community_checkin.account'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='id',
            field=models.UUIDField(default=uuid.UUID('70e2f30d-4343-4901-84dc-51bae28161da'), primary_key=True, serialize=False, unique=True),
        ),
    ]
