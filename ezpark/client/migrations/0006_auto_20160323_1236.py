# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_client_braintree_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='braintree_id',
            field=models.CharField(max_length=36, null=True),
        ),
    ]
