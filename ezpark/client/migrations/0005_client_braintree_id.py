# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='braintree_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
