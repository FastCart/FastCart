# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20170602_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastgoods',
            name='is_bought',
            field=models.BooleanField(default=False),
        ),
    ]
