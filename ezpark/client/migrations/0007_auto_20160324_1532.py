# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-24 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20160323_1236'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='transaction',
            order_with_respect_to='car',
        ),
    ]
